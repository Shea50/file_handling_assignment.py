with open("my_file.txt", "w") as file:
    # Write lines of text to the file
    file.write("Hello, my name is Brian.  ")
    file.write("I am 21 years old.  ")
    file.write("I live @ 75th street.")

print("Data has been written to my_file.txt.")


with open("my_file.txt", "r") as file:
    # Read and display the contents of the file
    file_contents = file.read()
    print("Contents of my_file.txt:")
    print(file_contents)

with open("my_file.txt", "a") as file:
    # Append three additional lines of text
    file.write("I am currently studying Computer Science. ")
    file.write("I enjoy playing football in my free time. ")
    file.write("I have 3 siblings. ")

print("Additional data has been appended to my_file.txt.")

with open("my_file.txt", "r") as file:
    # Read and display the contents of the file
    file_contents = file.read()
    print("Contents of my_file.txt:")
    print(file_contents)

try:
    # Open the file in write mode ('w') to initially write data
    with open("my_file.txt", "w") as file:
        # Write lines of text to the file
        file.write("Hello, I am Alicia. ")
        file.write("I am Brian's Sister. ")
        file.write("I also live @ 75th Street. ")

    print("Initial data has been written to my_file.txt.")

    # Open the file in append mode ('a') to append additional data
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text
        file.write("I am currently in High School. ")
        file.write("My favorite subject is Biology. ")
        file.write("My best friend's name is Shirley. ")

    print("Additional data has been appended to my_file.txt.")

    # Open the file in read mode ('r') to read the updated contents
    with open("my_file.txt", "r") as file:
        # Read and display the updated contents of the file
        file_contents = file.read()
        print("Updated contents of my_file.txt:")
        print(file_contents)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied to access the file.")

finally:
    print("File handling completed.")