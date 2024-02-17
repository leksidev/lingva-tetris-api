from database import new_session
from model import WordOrm

from sqlalchemy import select
from schemas import SWordAdd, SWord


class WordRepository:
    @classmethod
    async def add_word(cls, word: SWordAdd) -> int:
        async with new_session() as session:
            data = word.model_dump()
            new_word = WordOrm(**data)
            session.add(new_word)
            await session.flush()
            await session.commit()
            return new_word.id

    @classmethod
    async def get_words(cls) -> list[SWord]:
        async with new_session() as session:
            query = select(WordOrm)
            result = await session.execute(query)
            word_models = result.scalars().all()
            words = [SWord.model_validate(word_model) for word_model in word_models]
            return words
