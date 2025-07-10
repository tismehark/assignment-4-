
file = open('output.txt', 'w')
writing_file = file.write("hello python ")
print(writing_file)
file.close()

file = open('output.txt', 'r')
reading_file = file.read()
print(reading_file)
file.close()

file=open('output.txt', 'a')
appending_file=file.write("\nlearning file handling in python")
print(appending_file)
file.close()

file = open('output.txt', 'r')
reading_file = file.read()
print(reading_file)
file.close()

