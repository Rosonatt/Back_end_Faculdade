from fastapi import FastAPI
from routers.product_router import router as product_router

app = FastAPI()

app.include_router(product_router)

@app.get("/")
def inicio():
    return {"mensagem": "tentei professor"}