# activity 1
# file= open("text.txt","r")
# print(file.read(30))
# file= open("text.txt","a")
# file.write("Beyblad x is coming")
# activity 2
# file= open("text.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# for i in file:
#     print(i)
file1= open("text.txt","r")
file2= open("abc.txt","w")
for line in file1.readlines():
    if not (line.startswith("coding")):
        print(line)
        file2.write(line)