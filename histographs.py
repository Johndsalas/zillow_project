
from env import host, user, password
import pandas as pd

def wrangle_zillow_graphs():

    database = "zillow"

    def get_db_url(user,host,password,database):

        url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
        return url

    url = get_db_url(user,host,password,database)

    query = """ 
            SELECT fips, taxvaluedollarcnt as "Tax_value", taxamount as 'Tax_Amount', round(taxamount/taxvaluedollarcnt, 3) as 'Tax_Rate'
            FROM properties_2017

            JOIN predictions_2017
            USING (id)

            JOIN propertylandusetype
            USING (propertylandusetypeid)

            WHERE propertylandusedesc in ('Residential General','Single Family Residential', 'Rural Residence', 'Mobile Home', 'Bungalow', 'Manifactured, Modular, Prefabricated Homes', 'Patio Home', 'Inferred Single Family Residential' )

            AND transactiondate between '2017-05-01' and '2017-06-31'

            AND fips = '6037'

            AND taxvaluedollarcnt is not null;       
            """

    df = pd.read_sql(query, url)

    df = df.astype(float)

    return df


def wrangle_zillow_graphs2():

    database = "zillow"

    def get_db_url(user,host,password,database):

        url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
        return url

    url = get_db_url(user,host,password,database)

    query = """ 
            SELECT fips, taxvaluedollarcnt as "Tax_value", taxamount as 'Tax_Amount', round(taxamount/taxvaluedollarcnt, 3) as 'Tax_Rate'
            FROM properties_2017

            JOIN predictions_2017
            USING (id)

            JOIN propertylandusetype
            USING (propertylandusetypeid)

            WHERE propertylandusedesc in ('Residential General','Single Family Residential', 'Rural Residence', 'Mobile Home', 'Bungalow', 'Manifactured, Modular, Prefabricated Homes', 'Patio Home', 'Inferred Single Family Residential' )

            AND transactiondate between '2017-05-01' and '2017-06-31'

            AND fips = '6059'

            AND taxvaluedollarcnt is not null;       
            """

    df = pd.read_sql(query, url)

    df = df.astype(float)

    return df


def wrangle_zillow_graphs3():

    database = "zillow"

    def get_db_url(user,host,password,database):

        url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    
        return url

    url = get_db_url(user,host,password,database)

    query = """ 
            SELECT fips, taxvaluedollarcnt as "Tax_value", taxamount as 'Tax_Amount', round(taxamount/taxvaluedollarcnt, 3) as 'Tax_Rate'
            FROM properties_2017

            JOIN predictions_2017
            USING (id)

            JOIN propertylandusetype
            USING (propertylandusetypeid)

            WHERE propertylandusedesc in ('Residential General','Single Family Residential', 'Rural Residence', 'Mobile Home', 'Bungalow', 'Manifactured, Modular, Prefabricated Homes', 'Patio Home', 'Inferred Single Family Residential' )

            AND transactiondate between '2017-05-01' and '2017-06-31'

            AND fips = '6111'

            AND taxvaluedollarcnt is not null;       
            """

    df = pd.read_sql(query, url)

    df = df.astype(float)

    return df