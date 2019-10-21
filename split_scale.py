from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def split_my_data(x, y, train_pct):

    x_train, x_test, y_train, y_test =  train_test_split(x,y, train_size = train_pct, random_state = 999)

    return x_train, x_test, y_train, y_test


def standard_scaler(train,test):

    scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)

    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])

    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

    return train_scaled, test_scaled, scaler