def modify_string(original):
 original += " that has been modified."
 # At the moment, only the local copy of this string has been modified
def modify_string_return(original):
 original += " that has been modified."
 # However, we can return our local copy to the caller. The function
 # ends as soon as the return statement is used, regardless of where it
 # is in the function.
 return original
test_string = "This is a test string"
modify_string(test_string)
print(test_string)
test_string = modify_string_return(test_string)
print(test_string)