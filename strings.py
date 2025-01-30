"""
SUBSTRING EXTRACTION
"""
#provided string to extract
string = "Hello beautiful, how are you doing today?"
print(string)

#get user indices
indice_1 = int(input("Enter first indice: "))
indice_2 = int(input("Enter second indice: "))

#extract the substring using the given indices
extraction = string[indice_1:indice_2]
print(f"Extracted substring is: {extraction}")
print()

"""
Find character index
"""
#gets a string from the user
user_string = input("Enter a string: ")

#finds the index of the first occurence of a character in a string

#find the first character
str_character = user_string[0]

#find the index
str_index = user_string.find(str_character)
print(f"The first character is on index: {str_index}")