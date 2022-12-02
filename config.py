import pandas as pd
import data

def load():
    df = pd.read_csv("gfg.txt", sep=" ")
    return df