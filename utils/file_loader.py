import pandas as pd

def load_master_data():

    patients = pd.read_csv("output/PAT_DMGRPHC.csv")
    coverage = pd.read_csv("output/MBR_CVRG.csv")
    hospitals = pd.read_csv("output/HOSPITAL.csv")
    providers = pd.read_csv("output/PROVIDER.csv")

    return patients, coverage, hospitals, providers