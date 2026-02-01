from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get/{id}/")
async def root_two(id: int):
    return {"id": id}


@app.get("/health/")
async def get_health():
    return {"health": "ok"}
