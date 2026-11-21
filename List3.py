message = input("Enter a message that you would like to use as a palindrome: ")
reverse = message[::-1]
print("The original message is:", message)
print("The reverse of the message is:", reverse)
if message == reverse:
    print("The message is a palindrome.")
else:
    print("The message is not a palindrome.")