import numpy as np
import pandas as pd
from scipy import stats
from pydataset import data
from sklearn.model_selection import train_test_split
# import sys
# sys.path.append('/Users/mph/codeup-data-science/classification-exercises/')

def prep_telco(telco_df):
    telco_df = telco_df.T.drop_duplicates().T
    dummy_telco_df = pd.get_dummies(telco_df[['gender','contract_type','internet_service_type']], dummy_na=False, drop_first=[True, False, False])
    telco_df = pd.concat([telco_df, dummy_telco_df], axis=1)
    telco_df.senior_citizen = telco_df.senior_citizen.astype('int')
    telco_df.tenure = telco_df.tenure.astype('int')
    telco_df.monthly_charges = telco_df.monthly_charges.astype('float')
    telco_df.partner = telco_df.partner.map(dict(Yes=1, No=0))
    telco_df.dependents = telco_df.dependents.map(dict(Yes=1, No=0))
    telco_df.phone_service = telco_df.phone_service.map(dict(Yes=1, No=0))
    telco_df.paperless_billing = telco_df.paperless_billing.map(dict(Yes=1, No=0))
    telco_df.churn = telco_df.churn.map(dict(Yes=1, No=0))
    cols_to_drop = ['internet_service_type_id', 'contract_type_id', 'payment_type_id', 'gender']
    telco_df = telco_df.drop(columns=cols_to_drop)
    telco_df.total_charges = telco_df.total_charges.str.replace(' ', '0')
    telco_df.total_charges = telco_df.total_charges.astype('float')
    avg_monthly_charges = telco_df.monthly_charges.mean()
    avg_tenure = telco_df.tenure.mean()
    telco_df['bel_avg_ten_abv_avg_mon_chrg'] = (telco_df['monthly_charges'] > avg_monthly_charges) & (telco_df['tenure'] < avg_tenure)
    telco_df.bel_avg_ten_abv_avg_mon_chrg = telco_df.bel_avg_ten_abv_avg_mon_chrg.replace(True, 1)
    telco_df.bel_avg_ten_abv_avg_mon_chrg = telco_df.bel_avg_ten_abv_avg_mon_chrg.replace(False, 0)
    return telco_df

def split_data_telco(telco_df):
    train_telco, test_telco = train_test_split(telco_df, test_size=.2, random_state=123, stratify=telco_df.churn)
    train_telco, validate_telco = train_test_split(train_telco, test_size=.25, random_state=123, stratify=train_telco.churn)
    return train_telco, validate_telco, test_telco
