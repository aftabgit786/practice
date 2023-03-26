import os

def get_file_contents():

    file_contents = []

    file_name = input("Enter file name: ")  #f1.csv for t1 and t2 | f2.csv for t5 and t6
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "files", file_name)

    with open(file_path, "r") as file_reader:
        file_content = file_reader.read()

        for line in file_content.split("\n")[1:-1]:
            column = line.split(",")
            file_contents.append(column)

        file_reader.close()

    return file_contents
