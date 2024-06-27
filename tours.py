from . import Base, mapped_column, Mapped


class Tour(Base):
    __tablename__ = "tours"

    title: Mapped[str]
    short_description:Mapped[str]
    long_description:Mapped[str]
    direction:Mapped[str] 
    price:Mapped[int]


