from fastapi import fastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI()
fake = Faker()

file_name = "backend/fakeapi/products.csv"
df = pd.read_csv(file_name)
df["indice"] = range(1, len(df) + 1)
df.set_index("indice", inplace=True)

onlinestore = 11

@app.get("/shopping")
async def shopping():
    index = random.randint(1, len(df) - 1)
    tuple = df.iloc[index]
    return [
        {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": tuple["Product Name"],
            "ean": int(tuple["EAN"]),
            "price": round(float(tuple["Price"]) * 1.2, 2),
            "clientPosition": fake.location_on_land(),
            "store": onlinestore,
            "dateTime": fake.iso8601()
        }
    ]

@app.get("/shopping/{register_number}")
async def shopping(register_number: int):
    if register_number < 1:
        return{"error":"The number is bigger than 1"}
    
    respostas = []

    for _ in range(register_number):
        index = random.randint(1, len(df) - 1)
        tuple = df.iloc[index]
        compra = {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": tuple["Product Name"],
            "ean": int(tuple["EAN"]),
            "price": round(float(tuple["Price"]) * 1.2, 2),
            "clientPosition": fake.location_on_land(),
            "store": onlinestore,
            "dateTime": fake.iso8601(),
        }
        respostas.append(compra)

    return respostas