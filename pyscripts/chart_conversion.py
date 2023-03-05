import pandas as pd
import numpy as np

import json

def convert(df,row_number):
    df_mut = df
    
    df_mut["times"] = df.index.astype(np.int64) // 10**9
    df_mut.dropna(inplace=True, subset = [df_mut.columns[row_number]])
    

  
    json_data = {}
    json_data['data'] = []

    for index, row in df_mut.iterrows():
        json_data['data'].append({'x': row['times'], 'y': row[df_mut.columns[row_number]]})

    # k = str(json.dumps(json_data)).replace('"', '')
    k = json.dumps(json_data)

    return json_data

def full_convert(df, labels):
    json_data = {}
    json_data['dataset_1'] = []
    json_data['dataset_1'].append(convert(df,0))
    json_data['dataset_2'] = []
    json_data['dataset_2'].append(convert(df,1))
    json_data['labels'] = labels
    k = json.dumps(json_data)

    return str(k)
    
