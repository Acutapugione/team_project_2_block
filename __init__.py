from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine

engine = create_engine("mssql+pymssql://scott:tiger@hostname:port/my_db")

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True)


from .tours import Tour

def up():
    Base.metadata.create_all(engine)

def down():
    Base.metadata.drop_all(engine)

down()
up()