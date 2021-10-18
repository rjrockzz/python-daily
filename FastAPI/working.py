from fastapi import FastAPI, Path

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
def get_item(item_id: int = Path(description = "The id of the item we'd like to view")): # type-hint fastapi
    return inventory[item_id]
