from fastapi import FastAPI
from base import SecurePassword
import typing as t

app = FastAPI()
gen = SecurePassword()

@app.get("/")
def custom(
    length: t.Optional[int] = None,
    lower: t.Optional[int] = 1,
    upper: t.Optional[int] = 0,
    digits: t.Optional[int] = 0,
    symbols: t.Optional[int] = 0,
    ):
    
    return {
        "password": str(
            gen.password(
                length=length,
                lower=lower,
                upper=upper,
                digits=digits,
                symbols=symbols,
                )
            )
        }
    