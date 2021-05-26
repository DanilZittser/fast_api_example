import uvicorn

from environment import env
from fastapi import FastAPI
from models import NPImage

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World!'}


@app.post('/images/')
async def image_shape(npimage: NPImage):
    return {'image_shape': f'{npimage.image.shape}'}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=env.fastapi_host,
        port=env.fastapi_port,
        log_level=env.fastapi_log_level
    )
