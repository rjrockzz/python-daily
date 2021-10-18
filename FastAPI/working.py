from fastapi import FastAPI, Path, Query, HTTPException,status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None

class UpdateItems(BaseModel):
    name : Optional[str] = None
    price : Optional[int] = None
    brand : Optional[str] = None
inventory = {
    1 :{
        "name" : "Milk",
        "price" : 234.5,
        "brand" : "regular"
    },
    2 :{
        "name" : "Soap",
        "price" : 381,
        "brand" : "fiama"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None,description = "The id of the item we'd like to view")): # type-hint fastapi and an added description.
    return inventory[item_id]
# Test it out : http://127.0.0.1:8000/get-item/1

# #query params
@app.get("/get-by-name/{item_id}")
def get_by_name(*,item_id, name : Optional[str] = None, test : int): # make it optional  
                                              # use Optional as recommended 
                                              # in the typing docs
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail = "Item ID Not Found!")
# Test it out : http://127.0.0.1:8000/get-by-name/?name=Soap

# After adding the compulsory int argument : http://127.0.0.1:8000/get-by-name/?test=2&name=Milk

# After adding the item_id : http://127.0.0.1:8000/get-by-name/2?test=2&name=Soap

# Request and Post Body

@app.post("/create-item/{item_id}")
def create_item(item_id : int, item: Item):
    if item_id in inventory:
        return {"Error":"Item ID already exists!"}

    inventory[item_id] = {"name" : item.name, "price" : item.price, "brand" : item.brand}
    return inventory[item_id]

# updating an item : put request

@app.put("/update_item/{item_id}")
def update_item(item_id: int, item: UpdateItems):
    if item_id not in inventory:
        return {"Error": "Item does not exists for updates"}
    inventory[item_id].update(item)
    return inventory[item_id]

# delete method
@app.delete("/delete-item")
def delete_item(item_id : int = Query(... , description="The id of the item to be delete")):
    if item_id not in inventory:
        return {"Error":"ID does not exists"}
    del inventory[item_id]
    return {"Success": "Item deleted."}