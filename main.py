from fastapi import FastAPI
from dotenv import load_dotenv
from src.routes.api_v1 import setup_routes
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

print("Starting....")
load_dotenv()
origins = [
    "https://aulaia.lideradigital.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logging.basicConfig(
    filename='app.log',  # Log file name
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    level=logging.INFO  # Log level
)

setup_routes(app)