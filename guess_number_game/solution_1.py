max = 5

print('Hello, welcome to the game. You will be choosing a number between 1 and 9.')
print('You can only guess up to', max, 'times. \n')
import random

attempts = 0
a = random.randint(1,9)

while True:

  guess = int(input('please enter an interger to guess\n'))
  attempts += 1

  if guess == a:
    print('exectly correct! answer is', a)
  elif guess > a:
    print('guess is too big')
  else:
    print('guess is too small')
  
  exit = str(input('if you like to exit the game, please enter "Y".'))
  if exit == 'Y':
    print('you have exited the game. you have tried', attempts, 'times. correct answer is', a)
    break
  
