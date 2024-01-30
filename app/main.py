from fastapi import FastAPI

def create_app():

    app = FastAPI(debug=True)

    return app


app = create_app()


@app.get('/')
async def root():
    return {"message" : "Hello World"}


@app.get('/items/{item_id}')
def read_item(item_id : int, q : str | None = None):
    return {"item_id" : item_id, "q" : q}
