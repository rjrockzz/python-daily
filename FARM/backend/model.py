from pydantic import BaseModel
# helps to autocreate json schemas from our model

class ToDo(BaseModel):
    title : str
    description : str 