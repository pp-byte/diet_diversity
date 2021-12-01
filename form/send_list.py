import pandas as pd

def get_list():
    l=[]
    df=pd.read_csv('resources/recipe.csv')
    for i in df['recipe'].unique():
        l.append((i,i))
    return l