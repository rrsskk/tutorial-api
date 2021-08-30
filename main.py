
from fastapi import FastAPI

app = FastAPI()



@app.post("/item/",status_code=201)

async def create_item(name:str):
    return {"name":name}



