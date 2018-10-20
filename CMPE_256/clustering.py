import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering


data = pd.read_csv('cluster.csv')
print data
plt.figure(figsize=(11, 8))
x=0
type = ['ward','average','complete']
name = ['single-link','average-link','complete-link']
for i in type:
    plt.title("Hierarchical Clustering Dendogram for "+ str(name[x]))
    dend = shc.dendrogram(shc.linkage(data, method='complete'))
    print(dend)
    print('Showing the Dendogram for the clustering tyoe {}').format(name[x])
    plt.show()
    ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage=str(i))
    print(ac.fit_predict(data))
    plt.figure(figsize=(10, 7))
    plt.title("cluser using " + str(name[x]))
    plt.scatter(data['x'],data['y'], c=ac.labels_, cmap='rainbow')
    plt.show()
    x += 1