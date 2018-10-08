from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
from sklearn.externals.six import StringIO
from sklearn.tree import DecisionTreeClassifier


clf = DecisionTreeClassifier()

'''
with open('/Users/mattsmacbook/Downloads/playCricket.csv') as csv_file:
    data_list = list(csv.reader(csv_file))
    print data_list

f = data_list[1:]
'''
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

dtree = clf.fit(X, Y)

dot_data=StringIO()

export_graphviz(dtree, out_file='dt_vi_tree.dot',
                     feature_names=['Outlook', 'Temperature', 'Humidity', 'Wind'],
                     class_names=['play', 'not-play'],filled=True, rounded=True)

image = pydotplus.graph_from_dot_data(dot_data.getvalue())

Image(image.create_png())
dot_data.ge