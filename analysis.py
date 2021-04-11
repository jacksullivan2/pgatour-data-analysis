import pandas as pd 
from matplotlib import pyplot as plt 

filename = "C:\\Users\\Jack\\Desktop\\python_project_1\\data\\pgadata_2010_2018.csv"

df = pd.read_csv(filename, index_col='Player Name')
pd.set_option('display.max_columns', 17)


# Convert the NaN values in the Wins and Top 10 columns to 0's. This is critical because NaN values are ignored when 
# calculating statistics like the median and mean, which gives us upper biased results as their values should've been a 0 and 
# counted.
# Note that I have discovered as issue with the dataset. I ran print(df.head(50)) before converting the NaN values in the wins 
# and top 10 columns to 0's. I found that non-members of the PGA tour are automatically assigned NaN values for their wins, 
# top 10's, money, and points. See Kiradech Aphibarnrat's 2018 season where he had 2 top 10's and earned $484,734 which were both 
# inputted as NULL values. So, be aware that in converting all NaN's to zero in these two columns do not enitrely accurately 
# represent the data.
df['Wins'].fillna(0, inplace=True)
df['Top 10'].fillna(0, inplace=True)

print(df)
