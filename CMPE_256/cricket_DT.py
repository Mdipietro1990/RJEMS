from sklearn import tree
import graphviz

clf = tree.DecisionTreeClassifier()

X = [[1,2,3,4],
      [1,2,3,5],
      [6,2,3,4],
      [7,8,3,4],
      [7,9,10,4],
      [7,9,10,5],
      [6,9,10,5],
      [1,8,3,4],
      [1,9,10,4],
      [7,8,10,4],
      [1,8,10,5],
      [6,8,3,5],
      [6,2,10,4],
      [7,8,3,5]]

Y = ['not-play','not-play', 'play','play','play','not-play','play','not-play','play','play','play','play','play','not-play']

clf = clf.fit(X, Y)

dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=['Outlook','Temperatue','Humidity','Wind'],
                         class_names=['not-play','play'],
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph
