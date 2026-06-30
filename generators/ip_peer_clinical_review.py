import pandas as pd
import random
import os
from faker import Faker
from config import *

fake = Faker("en_US")

def generate_ip_peer_clinical_review():

    cases = pd.read_csv("output/PREAUTH_CASE.csv")

    specialties = [
        "Cardiology",
        "Neurology",
        "Orthopedics",
        "Oncology",
        "General Surgery",
        "Internal Medicine",
        "Pulmonology"
    ]

    outcomes = [
        "Approved",
        "Denied",
        "Modified"
    ]

    records = []

    for i, row in cases.iterrows():

        if random.random() > 0.30:
            continue

        records.append({

            "PEER_REVIEW_ID": f"PCR{i+1:08d}",

            "CASE_ID": row["CASE_ID"],

            "REVIEW_PHYSICIAN": fake.name(),

            "SPECIALTY": random.choice(specialties),

            "REVIEW_DATE": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),

            "OUTCOME": random.choice(outcomes),

            "COMMENTS": fake.sentence(nb_words=12)

        })

    df = pd.DataFrame(records)

    df.to_csv(
        os.path.join(
            OUTPUT_FOLDER,
            "IPPeerClinicalReview.csv"
        ),
        index=False
    )

    print(f"IPPeerClinicalReview : {len(df):,} rows generated")