import os
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

def main():
    load_dotenv()

    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    metadata = MetaData()

    personas = Table(
        "personas_sebastiancardona",  
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nombre", String(100)),
        Column("correo", String(150)),
        Column("ciudad", String(100)),
        Column("telefono", String(50)),
        Column("ocupacion", String(100)),
        Column("direccion", String(200)),
        Column("edad", Integer),
    )

    metadata.create_all(engine)

    fake = Faker("es_CO")
    BATCH = 5000
    TOTAL = 100000

    with engine.connect() as conn:
        for start in range(0, TOTAL, BATCH):
            data = []
            for _ in range(BATCH):
                data.append({
                    "nombre": fake.name(),
                    "correo": fake.email(),
                    "ciudad": fake.city(),
                    "telefono": fake.phone_number(),
                    "ocupacion": fake.job(),
                    "direccion": fake.address(),
                    "edad": fake.random_int(min=18, max=90),
                })

            conn.execute(personas.insert(), data)
            conn.commit()

if __name__ == "__main__":
    main()

