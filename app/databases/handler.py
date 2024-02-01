from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager


class DBHandler:

    def __init__(self, app: FastAPI = None, **kwargs):

        self._engine = None
        self._session = None

        if app is not None:
            self.initialise(app=app, **kwargs)

    def initialise(self, app: FastAPI, **kwargs):

        url = ""

        if not url:
            return
        
        poolRecycle = 900
        echo = True

        username = 'postgres'
        pwd = 'admin'
        host = '192.168.0.100'
        port = 5432
        db_name = 'tb_test'

        self._engine = create_engine(
            f'postgresql://{username}:{pwd}@{host}:{port}/{db_name}',
            echo=echo,
            pool_recycle=poolRecycle,
            pool_pre_ping=True
        )

        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

        @app.on_event("startup")
        def startup():
            self._engine.connect()
        
        @app.on_event("shutdown")
        def shutdown():
            self._session.close_all()
            self._engine.dispose()

    
    @contextmanager
    def scop_session(self):

        s = self._session()

        try:
            yield s
            s.commit()
        except:
            s.rollback()
            raise
        finally:
            s.close()
    

    def maintain_session(self):

        if self._session is None:
            raise Exception("called initialize")
        
        s = None

        try:
            s = self._session()
            yield s
        finally:
            s.close()


    @property
    def session(self):

        return self.maintain_session
    

    @property
    def engine(self):

        return self._engine
    

db = DBHandler()
Base = declarative_base()
