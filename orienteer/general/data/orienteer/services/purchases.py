from uuid import UUID
from datetime import timezone, datetime, timedelta

from orienteer.general.data.orienteer.repositories import purchases
from orienteer.general.data.products.base_product import Product

from ..database import async_session


async def create_purchase(user_id: UUID, product: Product):
    async with async_session() as db_session:
        purchase = await purchases.create_purchase(db_session, product.id, user_id, product.price)
        return purchase


async def get_purchase_cooldown(user_id: UUID, product: Product) -> timedelta | None:
    if product.cooldown is None:
        return None

    async with async_session() as db_session:
        purchase = await purchases.get_last_purchase_of_product(db_session, user_id, product.id)

        if purchase is None:
            return None

        if (product.cooldown + purchase.date) > datetime.now(timezone.utc):
            return (product.cooldown + purchase.date) - datetime.now(timezone.utc)
        else:
            return None
