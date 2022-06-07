from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from core.utils import Queue, File

app = FastAPI()


# @app.get('/')
# async def home():
#     return await Queue.get_all_queue()


@app.get('/')
async def test():
    queue = Queue()
    services = queue.get_all_queues()
    return await queue.get_one_queue(services)

@app.on_event("startup")
@repeat_every(seconds=30)
def startup():
    print('startup')
    File()

