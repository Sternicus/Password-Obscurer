import random
import string


print ("Lets obscure your password!"'\n')

passphrase = input("Please enter your password: ")


# get random password pf length 8 with letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in passphrase ) 
print('\n') 
print ("Here is your new obscured password!:  " '\n', password, '\n')
print ("P.S. KEEP IT SECRET!")
