from typing import Optional,List

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")

async def read_items(x_token: Optional[List[str]] = Header(None)):

    return {"x_token_values":x_token}

