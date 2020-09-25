import re
#module for carriying out regexp matching
from random import randint
#module for working with the replyList
print (":)*********************************:)")

print("Hello there! Before we begin, I think it would be nice to get your nickname")
nickname = input("Nickname goes here=> ")
print (nickname, "you are welcome to the palindrome checker game.")

print("\nKindly enter a word to confirm its palindromicity")
replyList = [
	"\n Have a nice day! Although I hope you come back \nwith new words.",
	"You kinda suck at this!",
	"I strongly suggest you learn to type properly.",
	"Wow! It seems your on fire today.",
	"Your obviously getting a medal after this one",
	"That's the spirit!",
	"Your quite good at this"
]#Just a random list where the return statements for each scenario is stacked




def palindrome():
	
	test = str(input("Enter word here=> ")).strip()
#obtaining the word from the user
	if palindrometest(test):
		print("\nWelldone!", test, "is a palindrome.")

		
	else:
		print("\nUnfortunately", test, "is not a palindrome.")
#validating the word based on the palindrometest function
		
		
	newTrial = str(input("\nwould you like to try again (y/n)? => "))
	if newTrial.startswith("y") or newTrial.startswith("Y"):
		print("\n******************************")
		print(replyList[randint(3, len(replyList)- 1)])
		palindrome()
	elif newTrial.startswith("n") or newTrial.startswith("N"):
		print(replyList[randint(0, len(replyList)-6)])
	else:
		print(replyList[randint(1, len(replyList) - 5)])
#just some random manipulation of the list given above.
#Each item in the list is printed based on the user input.
	


def palindrometest(test):
	
	
#Tried to match the pattern(accepts any alphabet) so it excludes any non-alphabet.
	
	min_index = 0
	max_index = len(test) - 1
	
	while min_index < max_index:
		if test[min_index] != test[max_index]:
			return False
		min_index += 1
		max_index -= 1
#while loop which ensures the word is a palindrome		

	pattern = r"/[a-zA-Z]"
	#The regexp pattern which ensures the user inputs
	#only alphabets
	

	if re.match(pattern,test):
		return True
#if statement which returns true provided
#the word(test) satisfies the regexp
		
	return True
#function returns true if it satisfies both requirements
	


palindrome()


	   