import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (24, 8)

# simulate normal data 100*5
data = pd.read_csv('Pisa201520182022_GameDataset-2.csv', sep = ";")


print(data.describe())
