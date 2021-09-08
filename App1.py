# -*- coding: utf-8 -*-
# @Author: zhangxianqiao
# @Date:   2021-09-06 17:10:20
# @Last Modified by:   zhangxianqiao
# @Last Modified time: 2021-09-07 21:40:44


import json 
from difflib import get_close_matches

  
data = json.load(open("data.json"))

def word_lookup(word): 
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Did you mean %s instead? Enter Y for yes, or N for no: " % get_close_matches(word, data.keys())[0])
		if yn == "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == "N":
			return "Sorry, the word doesn't exist. Please check it again."
		else:
			return "We didn't understand your entry. Please try again."


	else:
		return "Sorry, the word doesn't exist. Please check it again."

word = input("Please enter a word: ")

output = word_lookup(word)

i = 1

if type(output) == list:
	
	for item in output:
		print(str(i)+". "+item)
		i += 1

else:
	print(output)




