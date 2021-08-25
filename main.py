from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
     return{"message" : "Hello World"}

@app.get("/item/{item_index}")    
async def read_item(item_id:int): # declairs the type of path parameter
    return{"item_id":"item_id"}

