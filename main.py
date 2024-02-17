from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables, fill_words_table
from router import router as words_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    await fill_words_table()
    print("База заполнена")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)
app.include_router(words_router)



