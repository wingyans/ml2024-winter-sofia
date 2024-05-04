
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
