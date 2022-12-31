#Random password generator
import random

#Set the password length
password_len= int(input("Please enter how many digit you want for your password?"))
#Set the password generator database
db="!@#$%^&*()1234567890QWERTYUIOPASDFGHJKLZXCVBNM<>?qwertyuiopasdfghjklzxcvbnm"
p = "".join(random.sample(db,password_len))
print(p)