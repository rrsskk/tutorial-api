
from fastapi import FastAPI,status

app = FastAPI()



@app.post("/item/",status_code=status.HTTP_201_CREATED)

async def create_item(name:str):
    return {"name":name}



