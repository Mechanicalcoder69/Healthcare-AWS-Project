from config import *
from generators.provider import generate_provider
from generators.preauth_case import generate_preauth_case
from generators.preauth_los import generate_preauth_los
from generators.preauth_los_rvw import generate_preauth_los_rvw
from generators.preauthrzn_days_rqstd import generate_preauthrzn_days_rqstd
from generators.preauth_case_flags import generate_preauth_case_flags
from generators.ip_peer_clinical_review import generate_ip_peer_clinical_review
from generators.ip_notifications import generate_ip_notifications
from generators.ip_member_letters import generate_ip_member_letters
from faker import Faker
import pandas as pd
import random
import os

# Initialize
fake = Faker("en_US")
Faker.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Common lists
states = ["TX","CA","NY","FL","IL","OH","NC","GA","AZ","PA"]

# ==================================================
# PAT_DMGRPHC
# ==================================================
print("Generating PAT_DMGRPHC...")

patient_records = []

lobs = ["Commercial","Medicaid","Medicare","Exchange","FEP"]
financial_companies = ["BCBS_TX","BCBS_CA","BCBS_FL","BCBS_IL","BCBS_NY"]
groups = ["Amazon","Google","Microsoft","Apple","Meta","Oracle","IBM","FedEx","Target","Walmart"]

for i in range(1, MEMBERS + 1):

    gender = random.choice(["Male","Female"])

    patient_records.append({
        "PAT_ID": f"PAT{i:07d}",
        "FIRST_NAME": fake.first_name_male() if gender == "Male" else fake.first_name_female(),
        "LAST_NAME": fake.last_name(),
        "DOB": fake.date_of_birth(minimum_age=1, maximum_age=90),
        "GENDER": gender,
        "MBR_LOB_NM": random.choice(lobs),
        "MBR_PLN_ST_CD": random.choice(states),
        "FNCL_CMPNY_CD": random.choice(financial_companies),
        "GRP_NM": random.choice(groups),
        "PAT_GRP_ID": f"GRP{random.randint(1,500):04d}"
    })

pd.DataFrame(patient_records).to_csv(
    os.path.join(OUTPUT_FOLDER, "PAT_DMGRPHC.csv"),
    index=False
)

print("PAT_DMGRPHC generated")

# ==================================================
# MBR_CVRG
# ==================================================
print("Generating MBR_CVRG...")

coverage_records = []

for i in range(1, MEMBERS + 1):

    coverage_records.append({
        "CVRG_ID": f"CVRG{i:07d}",
        "PAT_ID": f"PAT{i:07d}",
        "PLAN_ID": f"PL{random.randint(1,20):03d}",
        "COVERAGE_TYPE": random.choice(["Medical","Dental","Vision"]),
        "STATUS": random.choice(["Active","Inactive"]),
        "START_DATE": fake.date_between(start_date="-5y", end_date="-1y"),
        "END_DATE": fake.date_between(start_date="today", end_date="+2y")
    })

pd.DataFrame(coverage_records).to_csv(
    os.path.join(OUTPUT_FOLDER, "MBR_CVRG.csv"),
    index=False
)

print("MBR_CVRG generated")

# ==================================================
# HOSPITAL
# ==================================================
print("Generating HOSPITAL...")

hospital_records = []

for i in range(1, HOSPITALS + 1):

    hospital_records.append({
        "HOSPITAL_ID": f"HSP{i:05d}",
        "HOSPITAL_NAME": fake.company() + " Medical Center",
        "CITY": fake.city(),
        "STATE": random.choice(states),
        "BED_COUNT": random.randint(50,1000),
        "HOSPITAL_TYPE": random.choice([
            "Acute Care",
            "Children",
            "Specialty",
            "Teaching",
            "Community"
        ])
    })

pd.DataFrame(hospital_records).to_csv(
    os.path.join(OUTPUT_FOLDER, "HOSPITAL.csv"),
    index=False
)

print("HOSPITAL generated")

generate_provider()
generate_preauth_case()
generate_preauth_los()
generate_preauth_los_rvw()
generate_preauthrzn_days_rqstd()
generate_preauth_case_flags()
generate_ip_peer_clinical_review()
generate_ip_notifications()
generate_ip_peer_clinical_review()
generate_ip_member_letters()


print("\nAll files generated successfully!")