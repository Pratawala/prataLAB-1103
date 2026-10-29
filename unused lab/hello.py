print("========================================")
print("Welcome Here!")
print("My first post!")
print("========================================")

username =  "cool_creator"
bio = "Fun blogger"
followers = 100

followers += 50
print("day 1", followers)

followers += 20
print("day 2", followers)

followers -= 10 
print("day 3", followers)

username = input("Whats your username?")
age = input("what is your age?")
age = int(age)
category = input("What is your category?")

print ("\n Instagram profile")
print("=============")
print("Username:", username)
print("Bio:", age)
print("Category", category)

if age >=40 and category == "fun":
    print("You are old, what is fun to you?")