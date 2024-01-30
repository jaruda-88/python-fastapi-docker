from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

def create_app():

    app = FastAPI(debug=True)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()


@app.get('/')
async def root():
    return {"message" : "Hello World"}


@app.get('/items/{item_id}')
def read_item(item_id : int, q : str | None = None):
    return {"item_id" : item_id, "q" : q}
