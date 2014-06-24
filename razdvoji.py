dat1=open("kom.txt", "w")
dat2=open("rej.txt", 'w')
dat3=open("komentari.txt", "r")
poz = 0
neg = 0
neut = 0
for i in range(0,25871):
	dat3.readline()
	dat3.readline()
	dat3.readline()
	var = dat3.readline()
	var = var[9:12]

	if var == "1.0" or var == "1.5" or var == "2.0":
		dat2.write("0\n")
		neg+=1
	elif var == "2.5" or var == "3.0" or var == "3.5":
		dat2.write("1\n")
		neut+=1
	elif var == "4.0" or var == "4.5" or var == "5.0":
		dat2.write("2\n")
		poz+=1
	dat3.readline()
	dat3.readline()
	var = dat3.readline()
	var1 = var.split()
	var = " ".join(var1)
	var+= "\n"
	var = var.replace("<br>", " ")
	var = var.replace("&#39;", "'")
	dat1.write(var)
	dat3.readline()
	dat3.readline()


dat1.close()
dat2.close()
dat3.close()
print "\nnegativno = "
print neg
print "\nneutralno = "
print neut
print "\npozitivno = "
print poz

