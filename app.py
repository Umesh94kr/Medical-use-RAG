from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field 
from typing import Annotated
from Medical_RAG.rag import RAG

class UserInput(BaseModel):
    query: Annotated[str, Field(..., description="User query about medical problems : ")]


app = FastAPI()
rag = RAG()

@app.get('/ask_query')
def ask_query(data: UserInput):
    query = data.query
    response = rag.main(query)
    return JSONResponse(status_code=200, content={'response': response})
