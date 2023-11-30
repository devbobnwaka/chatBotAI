from pydantic import BaseModel
from datetime import datetime



class FlightBase(BaseModel):
    airline_name : str
    flight_number : str
    departure_airport : str
    arrival_airport : str
    departure_datetime : datetime
    arrival_datetime : datetime

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    pass

    class Config:
        orm_mode = True