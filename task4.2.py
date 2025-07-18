# Assignment4 from Module5, TASK2
# Wite and append data to the file

user_input1 = input("Enter text to write to the file: ")

file = open("output.txt", "w")
file.write(user_input1 + "\n")
file.close()
print("Data successfully written... \n")

user_input2 = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(user_input2 + "\n")
file.close()
print("Data successfully appended... \n")

file = open("output.txt", "r")
final_content = file.read()
file.close()

print("\nFinal content of output.txt:")
print(final_content)