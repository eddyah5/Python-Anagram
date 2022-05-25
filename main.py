# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
# the sorted strings are checked
	if(sorted(word1)== sorted(word2)):
		print("True")
	else:
		print("False")		
		
# Test/Compare
word1 ="hello"
word2 ="racecar"
find_anagrams(word1, word2)

#When word1=hello and word2 = ellho OUTPUT = TRUE