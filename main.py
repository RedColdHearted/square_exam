from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import SquareRepository
from square import schemas
from square import Square

app = FastAPI()

templates = Jinja2Templates(directory="templates")
db = SquareRepository()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/create_square/", response_model=schemas.SquareBase)
def create_square(square: schemas.SquareBase):
    return db.add(
        Square(
            x=square.x,
            y=square.y,
            side_length=square.side_length,
        )
    )

@app.get(
    "/get_square/{square_index}/",
    response_model=schemas.SquareBase,
)
def get_square(square_index: int):
    return db.get(square_index)

@app.post("/delete_square/{square_index}/")
def delete_square(square_index: int):
    return db.remove(square_index)

@app.get(
    "/get_all_squares/",
    response_model=dict[int, schemas.SquareBase],
)
def get_all_squares():
    return db.get_all()
