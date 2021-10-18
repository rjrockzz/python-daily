from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()

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
    return {"Sorry Arjun" : "Not Found"}
# Test it out : http://127.0.0.1:8000/get-by-name/?name=Soap

# After adding the compulsory int argument : http://127.0.0.1:8000/get-by-name/?test=2&name=Milk

# After adding the item_id : http://127.0.0.1:8000/get-by-name/2?test=2&name=Soap