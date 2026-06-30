from faker import Faker
import pandas as pd
import random
import os
from config import *

fake = Faker("en_US")

states = ["TX","CA","NY","FL","IL","OH","NC","GA","AZ","PA"]

specialties = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Oncology",
    "General Surgery",
    "Internal Medicine",
    "Pediatrics",
    "Emergency Medicine",
    "Psychiatry",
    "Pulmonology"
]

def generate_provider():

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    providers = []

    for i in range(1, PROVIDERS + 1):

        providers.append({

            "PROVIDER_ID": f"PRV{i:06d}",

            "PROVIDER_NAME": fake.name(),

            "NPI": random.randint(1000000000,9999999999),

            "SPECIALTY": random.choice(specialties),

            "STATE": random.choice(states),

            "HOSPITAL_ID": f"HSP{random.randint(1,HOSPITALS):05d}"

        })

    pd.DataFrame(providers).to_csv(
        os.path.join(OUTPUT_FOLDER,"PROVIDER.csv"),
        index=False
    )

    print("PROVIDER generated")