import csv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from model import Model, WordOrm
from schemas import SWordAdd

engine = create_async_engine("sqlite+aiosqlite:///words.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def fill_words_table():
    with open('words.csv', 'r') as f:
        en_ru_dict = csv.reader(f)
        async with new_session() as session:
            # async with engine.connect() as conn:
            for row in en_ru_dict:
                word = row[0].split(';')[0]
                translate = row[0].split(';')[1]
                new_row = WordOrm(word=word, translate=translate)
                session.add(new_row)
                await session.commit()
                await session.refresh(new_row)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
