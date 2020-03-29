from sqlalchemy import Column, String, DateTime, ForeignKey, create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

RDB_PATH = 'sqlite:///database.sqlite3'
engine = create_engine(RDB_PATH, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# クエリを扱う宣言
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'user'
    id = Column(
            'id',
            INTEGER(unsigned=True),
            primary_key=True,
            autoincrement=True,
        )
    username = Column('username', String(256))

class Task(Base):
    __tablename__ = 'task'
    id = Column(
            'id',
            INTEGER(unsigned=True),
            primary_key=True,
            autoincrement=True,
        )
    user_id = Column('user_id', ForeignKey('user.id'))
    content = Column('content', String(256))
    date = Column(
        'date',
        DateTime,
        default=func.now(),
        nullable=False,
        server_default=current_timestamp(),
    )
    done = Column('done', BOOLEAN, default=False, nullable=False)
