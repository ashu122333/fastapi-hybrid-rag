from typing import Optional
from fastapi import FastAPI, HTTPException
from hybrid_llm import query, upload

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Define a route without API key protection
@app.post("/query")
async def run_code(data: dict):
    # Extract input data from the request body
    input_data = data.get("input")
    conversation={}
    if not input_data:
        raise HTTPException(status_code=400, detail="Input data is required")
    
    conversation=data.get("conversation")
    
    # Process the input data and generate output
    output = query(input_data,conversation)
    return {"status": "success", "output": output}

@app.post("/upload")
def upload_chunks(data:dict):
    chunks=data.get("chunks")
    if not chunks:
        raise HTTPException(status_code=400, detail="chunks data is required")
    upload(chunks)
    return {"status":"success","output":"Documnets are uploaded are uploaded!!!"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
