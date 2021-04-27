#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

def get_number(text = 'please enter a number'):
  return int(input(text))

def determine_prime(number):
  divisors = []
  for divisor in range(2,number//2+1):
    if number%divisor == 0:
      divisors.append(divisor)
  if divisors == []:    
    print('it\'s a prime number.')
  else:
    print('this is not a prime number.')
    print('list of divisors is', divisors)    

while True:
  determine_prime(get_number())