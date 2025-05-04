course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
doubleQuote = "Python \"Programming\""
print(doubleQuote)
first = "Python"
last = "Programming"
print(f"{first} {last}")
print(course.upper())
print(course.strip())  # remove space
print(course.find('r'))  # find index of character
# returns boolean. Checks if the character exists in string and return boolean.
print('pro' in course)
print('rahul' not in course)
