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
