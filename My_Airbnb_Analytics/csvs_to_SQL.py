# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:04:37 2022

@author: avery
"""

import pandas as pd
import glob, os
from sqlalchemy import create_engine

for file in glob.glob("*.csv"):
    df = pd.read_csv(file)
    
    # Create SQLAlchemy engine to connect to MySQL Database
<<<<<<< HEAD:My_Airbnb_Analytics/csvs_to_SQL.py
    engine = create_engine("mysql+mysqldb://@localhost:3306/airbnb")
=======
    engine = create_engine("mysql+mysqldb:@localhost:3306/airbnb")
>>>>>>> 81ff1c1b6c0ef5aff142bc7e72a33c18f21c7157:Airbnb_Analytics/csvs_to_SQL.py

    
    # Convert dataframe to sql table                                   
    df.to_sql(file[:-4], engine, index=False)
    
    print('done')

    
    
