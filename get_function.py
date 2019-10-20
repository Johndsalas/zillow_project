import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm
import pandas as pd
import numpy as np
from scipy import stats
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

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
    
df = wrangle_zillow()

def split_my_data(x, y, train_pct):

    x_train, x_test, y_train, y_test =  train_test_split(x,y, train_size = train_pct, random_state = 999)

    return x_train, x_test, y_train, y_test


def standard_scaler(train,test):

    scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)

    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])

    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

    return train_scaled, test_scaled, scaler

#baseline_df=pd.DataFrame({'actual':series})

    
def baseline_mean_errors(df,column):
  
    df['baseline'] = df[column].mean()

    n = len(df)
   
    SSE_base = sum((df.baseline - df[column])**2)
    MSE_base = SSE_base / n
    RMSE_base = math.sqrt(MSE_base)

    df.drop(columns='baseline')

    return SSE_base, MSE_base, RMSE_base, n
        

def get_yhat(df,x_col,y_col):
    lr=LinearRegression()
    lr.fit(df[x_col],df[[y_col]])
    predictions=lr.predict(df[x_col])
    predictions_df = pd.DataFrame({'yhat':predictions.flatten()})
    
    return predictions_df


# def get_model_errors(yhat,y):

#     df['baseline'] = df[column].mean()
#     n = len(df)
   
#     SSE_base = sum((yhat - y)**2)
#     MSE_base = SSE_base / n
#     RMSE_base = math.sqrt(MSE_base)

#     return SSE_base, MSE_base, RMSE_base, n


def regression_errors(y, yhat):
    '''
    Returns a dictionary containing various regression error metrics.
    '''
    yhat['y']=y.reset_index(drop=True)
    yhat['residual']=yhat.yhat-yhat.y
    
    ybar = yhat['y'].mean()
    n = len(df)

    sse = sum(yhat.residual**2)
    mse = sse / n
    rmse = math.sqrt(sse / n)
    ess = ((yhat - ybar)**2).sum()
    tss = ess + sse
    
    return sse, mse, rmse, ess, tss

# yhat = Size_yhat
# y = y_train.Tax_Value.reset_index(drop=True)
# yhat['y']=y_train.Tax_Value.reset_index(drop=True)
# yhat['residual']=yhat.yhat-yhat.y