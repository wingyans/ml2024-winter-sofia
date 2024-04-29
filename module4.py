#prompt:
#The program asks the user for input N (positive integer) and reads it
#Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
#In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user input it before.


#solution:
#(1) program ask users to provide a positive integer N (used as total number of items that will be stored in the list)
#(2) create a blank list (provided_numbers) that can hold N number of items 
#(3) use a loop to ask user to enter the N numbers, one number each time (the number list will be updated with each number provided)
#(4) ask the user to provide target value X which would be compared against the list of numbers that was provided earlier
#(5) a for loop should be used in the search function to compare X against each entry in the list one by one
#(6) if a match is identified between X and the list, the match item's index position should be returned from the function 
#(7) if no match is found between X and the list, the function will return -1



#code: 
#matching function: 

def match_function(provided_numbers,X):
  for i in range(len(provided_numbers)):
        if provided_numbers[i] == X:
            return i + 1       #if matched, provide index position of the matched number
    # If the number is not found, return -1
    return -1         #if not matched, return -1 in the output



#ask for input main function: 

def main_function():
  N = int(input("Please enter the total number of values you want on the list (input must be a positive integer)."))
  provided_numbers = [] #empty list waiting for update
  for i in range(N):
        number_input = int(input(f"Please enter your {i+1} out of {N} number: ")) # prompt user to provide each value they want on the number list 
        provided_numbers.append(number_input) #each time the user provides a number, add it to the list 
  
  X  = int(input("Please enter your target value X in integer."))
  result = match_function(provided_numbers, X)
  print("Number matching result:",result)
  
  

#to execute the function: 
main_function()
