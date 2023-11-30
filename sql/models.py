from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime


from .database import Base

class FlightModel(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    airline_name = Column(String)
    flight_number = Column(String, index=True)
    departure_airport = Column(String)
    arrival_airport = Column(String)
    departure_datetime = Column(DateTime)
    arrival_datetime = Column(DateTime)