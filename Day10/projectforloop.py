
import os

folders = input("Please provide the list of folder names with followed by / :").split()


for folder in folders:

    try:
       files = os.listdir(folder)
    except FileNotFoundError:
        print("No such file or directory: Please provide valid folde!r name")
        break
    
    print("-- List of files in folder -" + folder)

    for file in files:
        print(file)


    







          






