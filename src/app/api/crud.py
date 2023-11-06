from app.api.models import ItemSchema, ItemRequest
from app.db import items, database
from app.config import logger
from datetime import datetime as dt


async def post(payload: ItemRequest):
    query = items.insert().values(
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
        created_date=dt.now().strftime("%Y-%m-%d %H:%M")
    )
    return await database.execute(query=query)


async def get(id: int):
    query = items.select().where(id == items.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = items.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload=ItemRequest):
    created_date = dt.now().strftime("%Y-%m-%d %H:%M")
    query = (
        items.update().where(id == items.c.id).values(
            title=payload.title,
            description=payload.description, completed=payload.completed,
            created_date=created_date
        )
        .returning(items.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = items.delete().where(id == items.c.id)
    return await database.execute(query=query)


async def example_error_db():
    logger.error("Something went wrong")
    try:
        raise KeyError("Something went wrong")
    except Exception as e:
        logger.exception(e)
    return 0
