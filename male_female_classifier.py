from sklearn import tree

#height, weight, shoe size
data = [[6,80,9],[6.1,90,10],[5.4,80,6],[5.7,85,7],[5.2,75,5],[5.3,48,5],[5.7,78,8],[5.8,75,7],[5.5,80,5]]

result = ['male','male','female','female','female','female','male','male','female']

clf = tree.DecisionTreeClassifier()

#training phase
clf = clf.fit(data,result)

#prediction
prediction = clf.predict([[7.12,80,6]])
print(prediction)
