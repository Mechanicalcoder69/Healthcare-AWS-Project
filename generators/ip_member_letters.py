import pandas as pd
import random
import os
from faker import Faker
from config import *

fake = Faker("en_US")

def generate_ip_member_letters():

    cases = pd.read_csv("output/PREAUTH_CASE.csv")

    letter_types = [
        "Approval",
        "Denial",
        "Additional Information",
        "Extension",
        "Cancellation"
    ]

    delivery_methods = [
        "Email",
        "Postal Mail",
        "Portal"
    ]

    records = []

    for i, row in cases.iterrows():

        # Around 75% of cases generate a member letter
        if random.random() > 0.75:
            continue

        if row["CASE_STATUS"] == "Approved":
            letter_type = "Approval"
        elif row["CASE_STATUS"] == "Denied":
            letter_type = "Denial"
        elif row["CASE_STATUS"] == "Cancelled":
            letter_type = "Cancellation"
        else:
            letter_type = "Additional Information"

        records.append({

            "LETTER_ID": f"LTR{i+1:08d}",

            "CASE_ID": row["CASE_ID"],

            "LETTER_TYPE": letter_type,

            "DELIVERY_METHOD": random.choice(delivery_methods),

            "LETTER_DATE": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),

            "LETTER_STATUS": "Sent"

        })

    df = pd.DataFrame(records)

    df.to_csv(
        os.path.join(
            OUTPUT_FOLDER,
            "IPmemberletters.csv"
        ),
        index=False
    )

    print(f"IPmemberletters : {len(df):,} rows generated")