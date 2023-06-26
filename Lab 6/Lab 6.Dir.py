import os
import string

# # 111111
# path = 'C:\\Users\\Акжол\\Desktop\\Coding\\Python\\LABs'
# dir_list = os.listdir(path)
# print("Only directories:")
# print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
# print("\nOnly files:")
# print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
# print('\n')
# print(dir_list)

# #  os.path.isdir() will return true or false depends on file or directory. if it is a file it will return false. if it is a directory it will return true.




# # 222222
# path = 'C:\\Users\\Акжол\\Desktop\\Coding\\Python\\LABs'
# print('Exist:', os.access('path', os.F_OK))
# print('Readable:', os.access('path', os.R_OK))
# print('Writable:', os.access('path', os.W_OK))
# print('Executable:', os.access('path', os.X_OK))






# # 333333
# print("Test a path exists or not:")
# path = 'C:\\Users\\Акжол\\Desktop\\Coding\\Python\\LABs\\Lab 6.Dir.py'
# print(os.path.exists(path))
# print("\nFile name of the path:")
# print(os.path.basename(path))
# print("\nDir name of the path:")
# print(os.path.dirname(path))




# # 444444
# f = open('newline.txt', 'r')
# cnt = 0
# Includes = f.read()
# CoList = Includes.split('\n')
# for i in CoList:
#     if i:
#         cnt+=1
# print(f"the number of lines: {cnt}")




# # 555555
# digit = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
# with open('digits.txt', 'w') as f:
#      for i in digit:
#         f.write(f'{i}\n')



# # 666666
# if not os.path.exists("letters"):
#    os.makedirs("letters")
# for letter in string.ascii_uppercase:
#    with open(letter + ".txt", "w") as file:
#        file.writelines(letter)




# # 777777
# with open('digits.txt',"r") as file:
#      with open('digits_2.txt',"w") as file1:
#           for i in file:
#               file1.write(i)
# content = open("digits_2.txt")
# print(content.read())




# # 888888
# path = 'C:\\Users\\Акжол\\Desktop\\Coding\\Python\\LABs\\file.txt'
# if os.path.exists(path):
#   os.remove(path)
# else:
#   print("The file does not exist")