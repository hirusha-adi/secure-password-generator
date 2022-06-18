from fastapi import FastAPI
from base import SecurePassword

app = FastAPI()
gen = SecurePassword()

@app.get("/")
def home():
    return {"password": str(gen.password())}