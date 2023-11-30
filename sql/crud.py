from sqlalchemy.orm import Session

from . import models, schemas


def get_flights(db: Session):
    return db.query(models.FlightModel).all()

def get_flights_by_destination(db: Session, departure : str, destination : str):
    return db.query(models.FlightModel).filter(models.FlightModel.departure_airport.ilike(departure)).filter(models.FlightModel.arrival_airport.ilike(destination)).all()

def create_flight(db: Session, flight: schemas.FlightCreate):
    db_flight = models.FlightModel(**flight.__dict__)
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight
