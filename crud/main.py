from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

data = []

class Item(BaseModel):
    name: str
    title: str
    author: str
    price: float


@app.post("/item/")
async def create_item(item: Item):
    data.append(item)
    return item

@app.get("/all-items/")
async def read_items():
    return data

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    try:
        return data[item_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

#In RESTful APIs, PUT replaces an entire resource with new data, while PATCH applies partial updates to a resource. PUT requires the entire resource to be sent in the request, even if some fields are unchanged, whereas PATCH only sends the fields that need to be modified. 

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    try:
        data[item_id] = item
        return item
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

# not working giving error 422 Unprocessable Entity
# @app.patch("/items/{item_id}")
# async def update_item_patch(item_id: int, item_update: Item):
#     try:
#         item = data[item_id]
#         item.name = item_update.name
#         item.title = item_update.title
#         item.author = item_update.author
#         item.price = item_update.price
#         return item
#     except IndexError:
#         raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    try:
        deleted_item = data.pop(item_id)
        return deleted_item
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")


