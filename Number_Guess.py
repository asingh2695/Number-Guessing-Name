import random
print("Hello, what is your name?")
name = input()
secretNumber=random.randint(1,100)
print("Hello {}, You will get 7 turns to guess the number that I am thinking of".format(name))
print('Hint: I am thinking of a number between 1 and 100')

for guessesTaken in range(1,7):
	print('Take a guess.')
	guess = int(input())
	if guess < secretNumber:
		print('Your guess is too low')
	elif guess > secretNumber:
		print('Your guess is too high')
	else:
		break
		
if guess == secretNumber:
	print('Good job, '+ name+' ! You have guessed my number in '+ str(guessesTaken)+' guesses')
else:
    print('Nope, the number I was thinking was '+ str(secretNumber))

input()
