from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Model(DeclarativeBase):
    pass


class WordOrm(Model):
    __tablename__ = "words"
    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str]
    translate: Mapped[str]
