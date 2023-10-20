from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
async def read_root():
    return FileResponse('template/index.html')

@app.get("/hola")
async def hola():
    return JSONResponse('El Domingo #confe')
