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
print(f"The first character is {str_character} on index: {str_index}")
print()

"""
Replace the character
"""

user_str = input("Enter a string: ")
char_to_replace = input("Enter a character you want to replace: ")
char_to_add = input("Enter the character you want to add: ")

#replace the string with the provided character
replaced = user_str.replace(char_to_replace, char_to_add)
print(f"""You replaced {char_to_replace} with {char_to_add}
Your string is now: {replaced}""")