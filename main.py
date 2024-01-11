from typing import Union

from fastapi import FastAPI

app = FastAPI()


# display html
#route_homepage.py

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from aminGPTapp import chat

from fastapi import FastAPI

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()
tts_route = APIRouter()





@general_pages_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("/speechjs.html",{"request":request})


@general_pages_router.get("/amin")
async def home(request: Request):
	return templates.TemplateResponse("/speechjs_amin.html",{"request":request})
	


@app.get("/hello")
def read_root():
    return {"Hello": "Amin"}

@tts_route.get("/speech")
def text_speech(q: Union[str, None] = None):
	answer = chat(q)
	return {"text": answer}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




def include_router(app):
	app.include_router(general_pages_router)
	app.include_router(tts_route)


def start_application():
	app = FastAPI()
	include_router(app)
	return app 

app = start_application()