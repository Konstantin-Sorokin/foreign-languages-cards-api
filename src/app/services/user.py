from sqlalchemy import select

from app.models import User
from app.services.base import BaseService


class UserService(BaseService):
    async def get_or_create_user(self, telegram_id: int) -> User:
        result = await self.session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()
        if user:
            return user

        user = User(telegram_id=telegram_id)
        self.session.add(user)
        await self.session.commit()
        return user
