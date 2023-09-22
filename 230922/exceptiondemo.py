import sys
sys.stdin = open('D:\PythonHome\230922\text01')

# first = int(input("Enter first Number : "))
# second = int(input("Enter second Number : "))

# try:
#     print(f"{first} / {second} = {first / second}")
# except Exception as err :
#     print(err)
# # else : 
# #     print("Job done")
# finally :
#     print("Program is Over")


#############
with open('D:\PythonHome\230922\text01', 'rt') as fread :
    try:
        count = 1
        for line in fread.realines() :
            print(f'{count} : {line}', end='')
            count += 1
    except :
        print('file not found')
    