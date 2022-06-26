from fastapi import FastAPI, Request
from fastapi_utils.tasks import repeat_every
from core.utils import Queue, File


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    queue = Queue()
    services = queue.get_all_queues()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "services": services,
    })





# @app.get('/services')
# def home():
#     queue = Queue()
#     return queue.get_all_queues()
#
#
# @app.get('/main')
# def test():
#     queue = Queue()
#     services = queue.get_all_queues()
#     return queue.get_one_queue(services)

@app.on_event("startup")
@repeat_every(seconds=30)
def startup():
    File()


