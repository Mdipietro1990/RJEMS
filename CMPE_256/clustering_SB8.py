import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from scipy.spatial import distance_matrix

data = pd.read_csv('SB_data.csv')

drink = data['PTIndex'].tolist()
time = data['HBIndex'].tolist()
label = data['label']

print data
datnp = np.column_stack([drink,time])
x = distance_matrix(datnp,datnp)
df = pd.DataFrame(x)
df.to_csv("/Users/mattsmacbook/Desktop/dist_matx.csv")


plt.figure(figsize=(11, 8))
type = ['ward','average','complete']
name = ['single-link','average-link','complete-link']
colors = ['red','green','blue']
x=0
for i in type:
    plt.title("Hierarchical Clustering Dendogram for "+ str(name[x]))
    dend = shc.dendrogram(shc.linkage(data, method=str(i)))
    print(dend)
    print 'Showing the Dendogram for the clustering tyoe {}'.format(name[x])
    plt.show()
    ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage=str(i))
    print(ac.fit_predict(data))
    plt.figure(figsize=(10, 7))
    plt.title("Cluser using " + str(name[x]))
    plot = plt.scatter(drink, time, c=ac.labels_,cmap=matplotlib.colors.ListedColormap(colors))
    cb = plt.colorbar(plot, spacing='proportional')
    loc = np.arange(0, max(label), max(label) / float(len(colors)))
    cb.set_ticks(loc)
    cb.set_ticklabels(colors)
    y=0
    for i in range(len(label)):
        plt.annotate(label[i], (drink[i], time[i]))
        y+=1
    plt.show()
    x += 1