phrase = input("Input words: ")
p
phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))