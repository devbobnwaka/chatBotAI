from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from bot import process_message
from sql import crud, models, schemas
from sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Message(BaseModel):
    msg: str

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chatbot/")
async def chatbot(msg: Message):
    response = process_message(msg.msg)
    return response

@app.get("/flights/{departure}/{destination}/")
async def get_flights(departure : str, destination : str, db: Session = Depends(get_db)):
    db_flight = crud.get_flights_by_destination(db, departure, destination)
    return db_flight

@app.post("/flights/", response_model=schemas.Flight)
async def create_flight(flight: schemas.FlightCreate, db: Session = Depends(get_db)):
    return crud.create_flight(db=db, flight=flight)
