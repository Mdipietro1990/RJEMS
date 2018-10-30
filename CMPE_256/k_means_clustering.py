import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from scipy.spatial import distance_matrix

data = pd.read_csv('k_mean_data.csv')

spendIdx = data['spending_index'].tolist()
incomeIdx = data['IncomeIndex'].tolist()
shopper = data['shopper'].tolist()
colors = ['r','g','b','purple']
marker = ['o','v','s','+']
formData = np.array(list(zip(spendIdx, incomeIdx))).reshape(len(spendIdx), 2)

plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('k_means data scatter plot')
plt.scatter(spendIdx,incomeIdx,c=shopper,cmap=matplotlib.colors.ListedColormap(colors))
plt.show()

# KMeans algorithm
K = 2
kmeans_model = KMeans(n_clusters=K).fit(formData)

plt.plot()
plt.title('k_means cluster plot with a K of ' + str(K))
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(spendIdx[i], incomeIdx[i], color=colors[l], marker=marker[l],ls='None')
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.annotate(shopper[i], (spendIdx[i], incomeIdx[i]))
plt.show()

