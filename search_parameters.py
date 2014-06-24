import numpy as np
import pylab as pl
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV

dat1 = open("komstem.txt", "r")
data = dat1.readlines()
Y = [int(line.replace("\n", "")) for line in open("rej.txt")]
data1=[]
Y1=[]

niz = [i for i in range(0,25871)]
r = random.sample(niz,  5000)
for i in r:
	data1.append(data[i])
	Y1.append(Y[i])

tf = TfidfVectorizer(norm="l2")
X1 = tf.fit_transform(data1)

selector = SelectKBest(chi2, 1000)
selector.fit(X1,Y1)
X = selector.transform(X1).todense()

C_range = 10.0 ** np.arange(-2, 9)
gamma_range = 10.0 ** np.arange(-5, 4)
param_grid = dict(gamma=gamma_range, C=C_range)
cv = StratifiedKFold(y=Y1, n_folds=10)
grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
grid.fit(X, Y1)

print("The best classifier is: ", grid.best_estimator_)

dat1.close()
