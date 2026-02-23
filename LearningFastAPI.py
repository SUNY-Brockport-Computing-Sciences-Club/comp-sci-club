from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define a FastAPI application object
app = FastAPI()

@app.get("/")
async def hello_root():
    return {"message": "Hello! Im learning FastAPI"}

'''
FastAPI gets item_id from the path which it'll then convert into a int
if that fails itll give a 400 error
'''
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

'''
This one has query parameters, so after /items/ you could put a ? for queries
for example, /items/?skip=6&limit=7 would set skip to 6 and limit to 7
'''
test_items = [{"item_name": "comp"}, {"item_name": "sci"}, {"item_name": "club"}]
@app.get("/items/")
async def list_items_with_skip(skip: int = 0, limit: int = 10):
    return test_items[skip: skip + limit]

'''
You can also have optional parameters with the None variable
Using None makes a query optional
'''
@app.get("/CollinIsCool/")
def read_optional(opt: str | None = None):
    if opt:
        return {"query": opt}
    return {"message": "Collin is so cool!"}

'''
If you're using a POST or a PUT route, basically any route that will
take a JSON body then you'll use Pydantic models to define and validate data
'''
movies_db = []
class Movie(BaseModel):
    id: int
    name: str
    description: str
    # Optional field
    year: int | None = None

'''
FastAPI will read the request which should be a JSON and then convert it to your
model, in this case the movie model. If a field is missing or the wrong
type then it'll give a 422 error.
'''
@app.post("/Movie/")
async def create_movie(movie: Movie):
    movies_db.append(movie)
    return movie

@app.get("/Movie/")
async def get_movie():
    if not movies_db:
        return {"message": "Movie not found"}
    return movies_db

@app.get("/Movie/{movie_id}")
async def get_movie_by_id(movie_id: int):
    for movie in movies_db:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

