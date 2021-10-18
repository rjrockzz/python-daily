from fastapi import FastAPI

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

@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name : str): # type-hint fastapi
    return inventory[item_id]
