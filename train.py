import pickle
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris_dataset = load_iris()

x = iris_dataset["data"]
y = iris_dataset["target"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, train_size = 0.8, shuffle = True)


clf = SVC()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

filename = 'model'
pickle.dump(clf, open(filename, 'wb'))

clf = pickle.load(open(filename, 'rb'))
y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))
