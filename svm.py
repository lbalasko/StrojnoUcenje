from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.feature_selection import SelectKBest, chi2
from numpy import * 


dat1 = open("komstem.txt", "r")
data = dat1.readlines()
vec = array([int(line.replace("\n", "")) for line in open("rej.txt")])
data = data
vec = vec

tf = TfidfVectorizer(norm="l2")
X1 = tf.fit_transform(data)

selector = SelectKBest(chi2, 1000)
selector.fit(X1,vec)
X = selector.transform(X1).todense()

clf = svm.SVC(C=10.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
  gamma=0.001, kernel='rbf', max_iter=-1, probability=False,
  random_state=None, shrinking=True, tol=0.001, verbose=False)
scores = cross_validation.cross_val_score(clf, X, vec, cv=10, scoring = "accuracy")

dat1.close()

x = arange(1,11)

for i in range(0,10):
	scores[i]=scores[i]*100;	

plt.figure()
plt.plot(x, scores, 'ro-')
plt.xlabel('N')
plt.ylabel('Tocnost')
ymin, ymax = plt.ylim()
plt.ylim( ymin-2, ymax+2 )
xmin, xmax = plt.xlim()
plt.xlim( xmin-0.2, xmax+0.2 )  
plt.title('SVM')

plt.savefig('SVM.png')

print(scores)
