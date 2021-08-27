

from fastapi import FastAPI,Path,Query


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(*,
item_id: int=Path(...,title="The id of item to get",ge=0,le=100),
    q:str, 
    Size:float= Query(...,gt=0,lt=10.5)):
    
    result = {"item_id": item_id}
    if q:
         
        result.update({"q": q})
    return result


    


   

