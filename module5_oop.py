class MatchFunction:
  def __init__(self):
    self.number_list = [] #create empty number list to hold user input numbers

  
  def get_list_length_N(self):
    
    while True:
      try:
        N = int(input("Enter the length of the list: "))
        if N > 0:
          return N
        else:
          print("Please enter a positive integer for number list length.")
      except ValueError:
        print("Number list length input invalid. Please enter a positive integer.")  




  def insert_num_input_N(self,N):
    
    print("Enter {} numbers:".format(N))
    for i in range(N):
      num = int(input("Enter number in position {}: ".format(i+1)))
      self.number_list.append(num)
      


  def get_check_value_X(self):
        X = int(input("Enter the value that you want to compare to the list: "))
        return X
       

  def validate_X(self,X):
    if X in self.number_list:
      return self.number_list.index(X) + 1 
    else:
      return -1 #no match found


def main():
    match_function = MatchFunction()
    N = match_function.get_list_length_N()
    match_function.insert_num_input_N(N)
    X = match_function.get_check_value_X()
    results = match_function.validate_X(X)
    if results != -1:
      print("The first match for your input number '{}' is at position {}.".format(X, results))
    else:
      print("No match found for {}.".format(X))



if __name__ == "__main__":
    main() #execute main function if the script is run directly

