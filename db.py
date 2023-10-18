import sqlalchemy
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import func
from sqlalchemy.orm import Session

import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()
__factory = None


def global_init(connection_string):
    global __factory

    if __factory:
        return

    conn_str = connection_string
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()


class Question(SqlAlchemyBase):
    __tablename__ = 'questions'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    question_text = sqlalchemy.Column(sqlalchemy.String)
    answer_text = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
