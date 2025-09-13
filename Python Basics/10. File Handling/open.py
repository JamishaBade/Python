file = open(
    "/Users/jamishabade/Desktop/python/Python Basics/10. File Handling/file.txt", "r"
)
content = file.read()
print(content)
file.close()

file = open(
    "/Users/jamishabade/Desktop/python/Python Basics/10. File Handling/file.txt", "w"
)
file.write("Hello, world!\n")
file.write("This is Python file handling.")
file.close()  # Always close the file
