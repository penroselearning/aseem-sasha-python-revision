# strings 

# string indexes

#         0123456789
mammal = "POLAR BEAR"

print(mammal[0])
print(mammal[1])
print(mammal[2])
print(mammal[3])
print(mammal[4])

# string methods

# strip() - removes any additional space before and after the string 

name = "   Eric  ".strip()

# print("Mr.",name.strip(),".")
print("Mr.",name,".")


# lower() - changes all the chracter of the string to lowercase

print(name.lower())

# upper() - changes all the chracter of the string to uppercase

print(name.upper())

# title() - changes all the chracter of the string to titlecase

print(name.title())

# split() - get certain information from the string by a specific character

fullname = "Deacon St.John"
# split_fullname = fullname.split(" ")
firstname, lastname = fullname.split(" ")

print(firstname)

# len() - returns the length of the string -> how many characters are there in a string (it also works with lists)

print(len(fullname))

# replace() - replaces a string to our specified string 

pm_of_nz = "Mrs. Jacinda Ardern"
pm_of_nz = pm_of_nz.replace("Mrs.", "").strip()

print("Prime Minister Of New Zealand:",pm_of_nz)
print(pm_of_nz)