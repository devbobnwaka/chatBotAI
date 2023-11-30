from neuralintents.assistants import BasicAssistant
from fastapi import Depends
from sqlalchemy.orm import Session
from sql.database import SessionLocal
from sql.crud import get_flights_by_destination, get_flights

import time
from utils import formatted_time

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

stocks = ['AAPL', 'META', 'TSLA', 'NVDA']

def print_stocks():
    print(f'Stocks: {stocks}')

assistant = BasicAssistant('intents.json')

# assistant = BasicAssistant('intents.json', method_mappings={
#     "stocks": print_stocks,
#     # "goodbye": lambda: process_message(db, available_flights=T),
# })

assistant.fit_model(epochs=50)
assistant.save_model()


def process_message(message):
    response = assistant.process_input(message)
    if response == "travel_location":
        dest = message.split()
        departure = dest[1]
        destination = dest[3]
        # print(departure, destination)
        db = next(get_db())
        results = get_flights_by_destination(db=db, departure=departure, destination=destination)
        # print(result[0].airline_name)
        if len(results) > 0:
            response = "Here are the available Flights: "
            for index, result in enumerate(results):
                response += f"""
                {index+1}. {result.airline_name} 
                flight_number : {result.flight_number}
                departure_airport : {result.departure_airport}
                arrival_airport : {result.arrival_airport}
                departure_datetime : {formatted_time(result.departure_datetime)}
                arrival_datetime : {formatted_time(result.arrival_datetime)}
                """
        else:
            response = "There are no available Flights found"
        print(response)
    if response == "all_travels":
        db = next(get_db())
        results = get_flights(db=db)
        if len(results) > 0:
            response = "Here are the available Flights: "
            for index, result in enumerate(results):
                response += f"""
                {index+1}. {result.airline_name} 
                flight_number : {result.flight_number}
                departure_airport : {result.departure_airport}
                arrival_airport : {result.arrival_airport}
                departure_datetime : {formatted_time(result.departure_datetime)}
                arrival_datetime : {formatted_time(result.arrival_datetime)}
                """
        else:
            response = "There are no available Flights found"
    return response

# done = False

# while not done:
#     message = input("Enter a message: ")
#     if message == "STOP":
#         done = True
#     else:
#         print(assistant.process_input(message))