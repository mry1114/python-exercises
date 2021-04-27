
#Write a program that asks the user how many Fibonnaci numbers to generate and then generates a list of them.
#Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

number = int(input('Please enter how many fibonacci number(s) to be genersted.\nWe will give you the highest number and a list of results. \nYour number:'))

def fib_number(count):
  
  if count == 0:
    result = 0
    return result
    
  elif count == 1:
    result = 1
    return result
    
  else:
    result = fib_number(count-1) + fib_number(count-2)
    return result
  
result = fib_number(number)

print('the', number, 'th fib result is', result)
    


def fib_list(count):

  fib = [1]
  
  while count > 1: #solution without introducing new variale i to limit the while loop
    fib.append(fib_number(count))
    count -= 1
  fib.sort() #sort list to get numbers from small to larg
  print('fib list is', fib)
  
fib_list(number)

