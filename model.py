
import math
import pandas as pd
from sklearn.linear_model import LinearRegression


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

def regression_errors(y, yhat):
    yhat['y']=y.reset_index(drop=True)
    yhat['residual']=yhat.yhat-yhat.y
    
    ybar = yhat['y'].mean()
    n = len(yhat)

    sse = sum(yhat.residual**2)
    mse = sse / n
    rmse = math.sqrt(sse / n)

    ess = sum((yhat.yhat - ybar)**2)
    tss = sse + ess
    r2 = ess/tss

    return sse, mse, rmse, r2

