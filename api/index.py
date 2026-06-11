from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# On Vercel, the app runs from api/index.py, so parent.parent is the root directory
BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="Arena 2.0",
    description="Premium mobile-ready 3D arena survival game.",
    version="2.0.0",
)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static"), check_dir=False), name="static")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")



