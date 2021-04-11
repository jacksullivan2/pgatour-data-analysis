import pandas as pd 
from matplotlib import pyplot as plt 

filename = "C:\\Users\\Jack\\Desktop\\python_project_1\\data\\pgadata_2010_2018.csv"

df = pd.read_csv(filename, index_col='Player Name')

