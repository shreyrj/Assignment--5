# function to check string
def check(s, arr):

	# returns a list of booleans
	result = [characters in s for characters in arr]
	return result


# Driver Code
s = "$shreyaaa23"
arr = ['e', 'r', '1', '$', '0']
print(check(s, arr))
