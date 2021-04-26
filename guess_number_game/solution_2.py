max = 3

print('Hello, welcome to the game. You will be choosing a number between 1 and 9.')
print('You can only guess up to', max, 'times.')
print('')
import random

attempts = 0
a = random.randint(1,9)

while attempts in range(0,max):

  guess = int(input('please enter an interger to guess'))
  attempts += 1

  if guess == a:
    print('exectly correct! answer is', a)
  elif guess > a:
    print('guess is too big')
  else:
    print('guess is too small')
  
else:
  print('sorry, you have exceeded the maximum attempts! correct answer is', a)
  