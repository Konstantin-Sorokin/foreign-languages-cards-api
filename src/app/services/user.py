from app.models import User
from app.services.base import BaseService


class UserService(BaseService):
    async def create_user(self, telegram_id: int) -> User:
        user = User(telegram_id=telegram_id)

        self.session.add(user)
        await self.session.commit()
        return user
