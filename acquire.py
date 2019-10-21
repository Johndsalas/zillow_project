import pandas as pd
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

    return df