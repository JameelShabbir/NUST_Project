# def vote():
#     age = input("Enter your age: ")

#     if int(age) >= 18:
#         print("you're able to marry with niaxy vee")
#     else:
#         print("You're not able to marry with niaxe vee")


# vote()
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


n = int(input("Enter a number : "))
fact = int(factorial(n))
print(f"The factorial of {n} is {fact}")

# Open a file for reading
file = open("learning.txt", "r")

# Perform operations on the file
content = file.read()
print(content)

# Close the file
file.close()
