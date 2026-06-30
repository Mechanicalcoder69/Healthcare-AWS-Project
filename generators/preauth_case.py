from utils.file_loader import load_master_data
from faker import Faker
import pandas as pd
import random
import os
from config import *

fake = Faker("en_US")

def generate_preauth_case():

    patients, coverage, hospitals, providers = load_master_data()

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    patient_ids = patients["PAT_ID"].tolist()
    hospital_ids = hospitals["HOSPITAL_ID"].tolist()
    provider_ids = providers["PROVIDER_ID"].tolist()
    plan_ids = coverage["PLAN_ID"].unique().tolist()

    case_status = [
        "Approved",
        "Pending",
        "Denied",
        "Cancelled"
    ]

    request_types = [
        "Inpatient",
        "Observation",
        "SNF"
    ]

    urgency = [
        "Routine",
        "Urgent"
    ]

    records = []

    for i in range(1, PREAUTH_CASES + 1):

        received = fake.date_between(
            start_date="-2y",
            end_date="today"
        )

        records.append({

            "CASE_ID": f"CASE{i:08d}",

            "PAT_ID": random.choice(patient_ids),

            "PLAN_ID": random.choice(plan_ids),

            "PROVIDER_ID": random.choice(provider_ids),

            "HOSPITAL_ID": random.choice(hospital_ids),

            "CASE_STATUS": random.choices(
                case_status,
                weights=[65,15,10,10]
            )[0],

            "REQUEST_TYPE": random.choices(
                request_types,
                weights=[70,20,10]
            )[0],

            "URGENCY": random.choices(
                urgency,
                weights=[80,20]
            )[0],

            "RECEIVED_DATE": received,

            "DECISION_DATE": fake.date_between(
                start_date=received,
                end_date="+30d"
            )

        })

    df = pd.DataFrame(records)

    df.to_csv(
        os.path.join(
            OUTPUT_FOLDER,
            "PREAUTH_CASE.csv"
        ),
        index=False
    )

    print(f"PREAUTH_CASE : {len(df):,} rows generated")