from sklearn.cross_validation import cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt
from numpy import *

dat1 = open("komstem.txt", "r")
data = dat1.readlines()
vec = array([int(line.replace("\n", "")) for line in open("rej.txt")])

tf = TfidfVectorizer(norm="l2")
X1 = tf.fit_transform(data)

selector = SelectKBest(chi2, 1000)
selector.fit(X1,vec)
X = selector.transform(X1).todense()

mnb = MultinomialNB()

scores = cross_val_score(mnb, X, vec, cv=10, scoring = "accuracy")

dat1.close()

x = arange(1,11)

for i in range(0,10):
	scores[i]=scores[i]*100;	

plt.figure()
plt.plot(x, scores, 'o-')
plt.xlabel('N')
plt.ylabel('Tocnost')
ymin, ymax = plt.ylim()
plt.ylim( ymin-2, ymax+2 )
xmin, xmax = plt.xlim()
plt.xlim( xmin-0.2, xmax+0.2 )  
plt.title('NaiveBayes')

plt.savefig('NaiveBayes.png')

print(scores) 
