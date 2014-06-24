from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop=stopwords.words('english')
dat1 = open("kom.txt", "r")
dat2 = open("komstop.txt", "w")

for i in range(0,25871):
	sentence = dat1.readline()
	sentence = sentence.replace(".", " ")
	sentence = sentence.replace(",", " ")
	sentence = sentence.replace("!", " ")
	sentence = sentence.replace("?", " ")
	sentence = sentence.replace("*", " ")
	var = [i for i in sentence.split() if i not in stop]
	var = " ".join(var)
	dat2.write(var)
	dat2.write("\n")

dat1.close()
dat2.close()

dat3 = open("komstop.txt", "r")
dat4 = open("komstem.txt", "w")

stemmer=PorterStemmer()
for i in range(0,25871):
	var = dat3.readline()
	var1 = " ".join([word.lower() for word in var.split() if word.isalpha()])
	var1 = " ".join([stemmer.stem(word) for word in var1.split()])
	var1 += "\n"
	dat4.write(var1)

dat3.close()
dat4.close()
