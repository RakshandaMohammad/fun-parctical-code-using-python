#Two-Player Random Number Game
# import random

# p1 = 0
# p2 = 0

# while p1 < 20 and p2 < 20:
#     input("Player 1, press ENTER : ")
#     p1 += random.randint(1, 6)
#     print("Player 1 =", p1)
    
#     if p1 >= 20:
#         print("Player 1 WINS!")
#         break

#     input("Player 2, press ENTER : ")
#     p2 += random.randint(1, 6)
#     print("Player 2 =", p2)
    
#     if p2 >= 20:
#         print("Player 2 WINS!")
#         break
# # creating password using choices
# import random
# a = 'abcdefghijklmnopqrstuvwxyz'
# n = '0123456789'
# s = '@#$%&*'
# n1 = int(input("Enter how many alphabets you want: "))
# n2 = int(input("Enter how many numbers you want: "))
# n3 = int(input("Enter how many special characters you want: "))

# password = ''.join(random.choices(a, k=n1) + random.choices(n, k=n2) + random.choices(s, k=n3))

# print( password)

#guessing number
# import random

# num = int(input("Enter a number (1-50): "))

# while True:
#     input("Press ENTER...")
#     r = random.randint(1, 50)
#     print(r)
#     if r == num:
#         print("Correct Guess!")
#         break
import random

while True:
    user = int(input("Enter a number (1-50): "))
    sys_num = random.randint(1, 50)
    print("System:", sys_num)
    if user == sys_num:
        print("🎉 Correct Guess!")
        break


