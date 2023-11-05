from fastapi import FastAPI
from pydantic import BaseModel
from bot import process_message

class Message(BaseModel):
    msg: str


app = FastAPI()


@app.post("/chatbot/")
async def chatbot(msg: Message):
    message = process_message(msg.msg)
    return message

