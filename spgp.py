import string
import random
import os
import time
import webbrowser
clear = lambda : os.system('cls')

print("Coded by imskidyo")
print("Discord Username: imskidyo")
print("Please wait 20 seconds!")
webbrowser.open('https://www.youtube.com/@imskidyo?sub_confirmation=1')
webbrowser.open('https://discord.gg/YEXg6Un2Dp')
time.sleep(20)
clear()
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)
print("Your generated password:", generated_password)
# Coded by imskidyo