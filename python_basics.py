"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if (num%2 == 0):
        print ("even")
    else:
        print ("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    randomnumber = random.randrange(1,10,1)
    userinput = input("Guess the number?")
    while (userinput != "exit"):
        if (int(userinput)> randomnumber):
            print ("too high")
        elif (int(userinput) < randomnumber):
            print ("too low")
        else:
            print ("exactly right")
        userinput = input("Guess the number?")


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    palindrome = True
    for i in range(0,int(len(string)/2)+1):
        if (string[i] != string[int(len(string))-1-i]):
            palindrome = False
    print (palindrome)


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    encodedBytes = base64.b64encode(username.encode("utf-8"))
    encodedusername = str(encodedBytes,"utf-8")
    encodedBytes = base64.b64encode(password.encode("utf-8"))
    encodedpassword = str(encodedBytes,"utf-8")
    file = open(filename,"w")
    file.write(encodedusername + "\n")
    file.write(encodedpassword)
    file.close()

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    file_object = open(filename, "r")
    encryptedusername = file_object.readline()
    encryptedpassword = file_object.readline()
    message_bytes = base64.b64decode(encryptedusername)
    decrypted_username = message_bytes.decode('utf-8')
    message_bytes = base64.b64decode(encryptedpassword)
    decrypted_password = message_bytes.decode('utf-8')
    print (decrypted_username)
    print (decrypted_password)
    file_object.close()
    if (password !=None):
        part4a(filename,decrypted_username, password)
        
        

if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
