def Replace(str1):
	maketrans = str1.maketrans
	final = str1.translate(maketrans(',.', '.,', ' '))
	return final.replace(',', ", ")
string = "32.054,23"
print(Replace(string))
