from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from bot import process_message

class Message(BaseModel):
    msg: str


app = FastAPI()


@app.post("/chatbot/")
async def chatbot(msg: Message):
    message = process_message(msg.msg)
    return message


if __name__ == "__main__": 
    # uvicorn main:app --reload
    uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)