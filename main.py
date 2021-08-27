

from fastapi import FastAPI,Path


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(*,item_id:int=Path(...,title="The id of item to get",ge=1),
    q:str):
    
    result = {"item_id":item_id}
    if q:
        result.update({"q": q})
    return result


    


   

