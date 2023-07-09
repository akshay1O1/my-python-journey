n=input("what is ur name")
print("hello "+n.upper())#makes the string stored in n an upper case string
print(n.replace(n,"AVENGERS"))#replaces the string with the word  temporarily
'''Print('i am ironman' in pwd) this will return bool  values'''
pwd=input("enter your password: ")
b="i am ironman" in pwd
if b==True:
    print("Welcome MR STARK")
elif "point break" in pwd:# this statement after elif returns bool and if it is true then condition is satisfied
    print("Welcome lord of thunder")
elif "strongest avenger" in pwd:
    print("welcome HULK")
else:
    print("wrong passsword")





