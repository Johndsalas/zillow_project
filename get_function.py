import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from env import host, user, password


def wrangle_zillow():

    database = "zillow"

    def get_db_url(user,host,password,database):

        url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
        return url

    url = get_db_url(user,host,password,database)

    query = """ 
            
            SELECT taxvaluedollarcnt as "Tax_Value", lotsizesquarefeet as "Size", bedroomcnt as "Bedrooms", bathroomcnt as "Bathrooms"
            FROM properties_2017

            JOIN predictions_2017
            USING (id)

            JOIN propertylandusetype
            USING (propertylandusetypeid)

            WHERE propertylandusedesc in ('Residential General','Single Family Residential', 'Rural Residence', 'Mobile Home', 'Bungalow', 'Manifactured, Modular, Prefabricated Homes', 'Patio Home', 'Inferred Single Family Residential' )

            AND transactiondate between '2017-05-01' and '2017-06-31'

            AND taxvaluedollarcnt is not null
            AND lotsizesquarefeet is not null
            AND bedroomcnt is not null
            AND bathroomcnt is not null         
            """

    df = pd.read_sql(query, url)

    df = df.astype(int)

    df.Tax_Value = df.Tax_Value.astype(float)

    return df

def split_my_data(x, y, train_pct):

    x_train, x_test, y_train, y_test =  train_test_split(x,y, train_size = train_pct, random_state = 999)

    return x_train, x_test, y_train, y_test


def standard_scaler(train,test):

    scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)

    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])

    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

    return train_scaled, test_scaled, scaler


def baseline_mean_errors(y):
    '''
    Returns a dictionary containing various regression error metrics for a
    baseline model, that is, a model that uses the mean of y as the prediction.
    '''
    yhat = y.mean()
    n = y.size
    residuals = yhat - y

    sse = sum(residuals ** 2)

    return {
        'sse: ' + sse,
        'mse: ' + sse / n,
        'rmse: ' + sqrt(sse / n),
    }