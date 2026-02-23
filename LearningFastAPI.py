from fastapi import FastAPI

# Define a FastAPI application object
app = FastAPI()

@app.get("/")
async def hello_root():
    return {"message": "Hello! Im learning FastAPI"}

'''
FastAPI gets item_id from the header which it'll then convert into a int
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