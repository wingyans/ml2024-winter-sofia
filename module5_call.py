from module5_mod import MatchFunction

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
