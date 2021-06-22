import pandas as pd
import numpy as np

def chargeData_ej0():
    try:
        root = '' 
        path = root + f'grupo_{Grupo}.txt'
        data = pd.read(path,sep='\t')
    except Exception as e:
        print(e)
    