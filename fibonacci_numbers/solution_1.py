#Write a program that asks the user how many Fibonnaci numbers to generate and then generates a list of them.
#Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

number = int(input('Please enter how many fibonacci number(s) to be genersted.\nWe will give you the highest number. \nYour number:'))

def fib_number(count):
  
  if count == 0:
    print("no fibonacci number is requested.")
  elif count > 0:
    result = 1
    if count == 1:
      print('fibonacci number is', result)
    else:
      prev_of_prev = 0
      prev = 1
      fib =[1]
      while count >= 2:
        # print('prev_of_prev = ', prev_of_prev)
        # print('prev = ', prev)
        result = prev_of_prev + prev
        
        prev_of_prev = prev
        prev = result
        fib.append(prev)

        count = count - 1
      print('fib list is', fib)
      
fib_number(number)

