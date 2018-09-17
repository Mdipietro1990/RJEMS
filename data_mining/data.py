import pandas as pd
import os

dataDir = '/Users/mattsmacbook/Downloads/all/'
dataFile = 'test.csv'
data_file = os.path.join(dataDir, dataFile)

f = pd.read_csv(data_file)

col = list(f.head(0))

f2 = pd.concat([pd.DataFrame([i], columns=['features']) for i in col])