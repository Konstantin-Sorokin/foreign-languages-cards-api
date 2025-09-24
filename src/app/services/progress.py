from datetime import datetime, timezone, timedelta
from typing import Annotated

from fastapi import Path
from sqlalchemy import func, select

from app.models.progress import Progress
from app.services.base import BaseService
from app.utils import increase_interval, decrease_interval


class ProgressService(BaseService):

    async def create_progress(self, user_id: int, card_id: int) -> None:
        progress = Progress(
            user_id=user_id,
            card_id=card_id,
            next_repeat=datetime.now(timezone.utc),
        )

        self.session.add(progress)

    async def get_all_need_progress(self, user_id: int) -> list[Progress]:
        stmt = (
            select(Progress)
            .where(Progress.user_id == user_id)
            .where(Progress.next_repeat <= func.now())
            .order_by(Progress.next_repeat)
        )
        all_progress = await self.session.scalars(stmt)
        return list(all_progress)

    async def update_progress(
        self,
        user_id: int,
        card_id: int,
        success: bool,
    ) -> None:

        stmt = select(Progress).where(
            Progress.user_id == user_id,
            Progress.card_id == card_id,
        )
        progress: Progress = await self.session.scalar(stmt)

        if success:
            interval_level, interval = increase_interval(progress.interval_level)
        else:
            interval_level, interval = decrease_interval(progress.interval_level)

        progress.next_repeat = datetime.now(timezone.utc) + timedelta(days=interval)
        progress.interval_level = interval_level

        await self.session.commit()
