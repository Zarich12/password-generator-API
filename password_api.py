from fastapi import FastAPI
from password_function import *

app =  FastAPI(title = 'API for password generator')

@app.get("/")
def generate():
    return {"password": password_generator() }