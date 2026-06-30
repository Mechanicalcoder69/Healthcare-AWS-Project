import pandas as pd
import random
import os
from faker import Faker
from config import *

fake = Faker("en_US")

def generate_ip_notifications():

    cases = pd.read_csv("output/PREAUTH_CASE.csv")

    notification_types = [
        "Email",
        "SMS",
        "Portal",
        "Fax"
    ]

    notification_status = [
        "Sent",
        "Delivered",
        "Failed"
    ]

    recipients = [
        "Member",
        "Provider",
        "Hospital"
    ]

    records = []

    for i, row in cases.iterrows():

        # Around 80% of cases generate a notification
        if random.random() > 0.80:
            continue

        records.append({

            "NOTIFICATION_ID": f"NTF{i+1:08d}",

            "CASE_ID": row["CASE_ID"],

            "NOTIFICATION_TYPE": random.choice(notification_types),

            "RECIPIENT": random.choice(recipients),

            "STATUS": random.choices(
                notification_status,
                weights=[80,15,5]
            )[0],

            "SENT_DATE": fake.date_between(
                start_date="-2y",
                end_date="today"
            )

        })

    df = pd.DataFrame(records)

    df.to_csv(
        os.path.join(
            OUTPUT_FOLDER,
            "IPnotifications.csv"
        ),
        index=False
    )

    print(f"IPnotifications : {len(df):,} rows generated")