# Assignment4 from Module5, TASK1
# Files, Exceptions, and Errors in Python

try:
    file = open("sample.txt" , "r")
    reading_file = file.readlines()

    print("Reading file content:")

    print("Line 1:" , reading_file[0])
    print("Line 2:" , reading_file[1])
    
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")