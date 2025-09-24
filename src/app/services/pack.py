from app.models import Pack
from app.services.base import BaseService


class PackService(BaseService):

    async def create_pack(
        self,
        name: str,
        description: str,
        card_type: str,
    ) -> Pack:
        pack = Pack(name=name, description=description, card_type=card_type)
        self.session.add(pack)
        await self.session.commit()
        return pack

    async def get_pack_by_id(self, pack_id: int) -> Pack | None:
        return await self.session.get(Pack, pack_id)
