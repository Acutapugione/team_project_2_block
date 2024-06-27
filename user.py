from . import Base, mapped_column, Mapped


class User(Base):
    __tablename__ = "users"

    nickname:Mapped[str] = mapped_column(unique=True)
    password:Mapped[str] = mapped_column(unique=True)
    
