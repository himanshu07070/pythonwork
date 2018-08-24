from sys import argv#this take argument from user
script , filename = argv#by this argument asign  easily in in order
txt = open(filename)#opening of file
print(f"here is your file{filename}:")
print(txt.read())#reading of file and then printing of that file
print("type the file name again:")
file_again = input(" >")#taking input from user
txt_again = open(file_again)#again opening of file
print(txt_again.read()) #again reading of file 