from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from databases import handler, models, functions
from sqlalchemy.orm import Session


def create_app():

    app = FastAPI(debug=True)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    handler.db.initialise(app)

    models.Base.metadata.create_all(bind=handler.db.engine)

    return app


app = create_app()


@app.get('/')
async def root():
    return {"message" : "Hello World"}


@app.get('/data/{data_id}', response_model=functions.Res)
def read_item(data_id : int, session: Session = Depends(handler.db.session)):

    data = session.query(models.BBS).filter(models.BBS.id == data_id).first()

    return data


@app.post('/new_data/', response_model=functions.Res)
async def register_test(data: functions.TestCreate, session: Session = Depends(handler.db.session)):
    data = models.BBS(**data.dict())

    session.add(data)
    session.flush()

    session.commit()

    return data

