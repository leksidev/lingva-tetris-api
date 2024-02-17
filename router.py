from fastapi import APIRouter, Depends

from repository import WordRepository
from schemas import SWordAdd, SWordId, SWord

router = APIRouter(
    prefix="/words",
    tags=["Слова"],
)


@router.post("")
async def add_word(word: SWordAdd = Depends()) -> SWordId:
    new_word_id = await WordRepository.add_word(word)
    return SWordId(id=new_word_id)


@router.get("")
async def get_words() -> list[SWord]:
    words = await WordRepository.get_words()
    return words
