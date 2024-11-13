# Lists, Dictionaries, tuples, sets, strings #
# String

# a = "Hello"
# b = "World"

# formatted = f"{a} {b}"
# print(formatted)

# print(a[1:4])
# print(a.upper())

# a = "Hello,world"
# print(a.split(","))

# Lists

# usernames = ["masterxx", "neo"]
# usernames.append("yoda")
# usernames.remove("neo")
# print(usernames)

# # usernames.sort()
# usernames.reverse()

# user_profile = {
#     "username": "yoda",
#     "location": "stockholm",
#     "favorite_places": ["Midgard", "Asgard"]
# }

# user_profile["favorite_places"].append("Helheim")

# user_profile["location"] = "Linköping"
# user_profile["email"] = "test@test.se"
# print(user_profile)

# coordinates = (10, 20)

# user1_favorites = {"Inception", "The Matrix", "Lord of the Rings", "Star Wars"}
# user2_favorites = {"The Matrix", "Interstellar", "Lord of the Rings", "Blade Runner"}

# common_favorites = user1_favorites & user2_favorites
# print(common_favorites)

# unique1 = user1_favorites - user2_favorites
# print(unique1)

# all = user1_favorites | user2_favorites
# print(all)

# Files, Operators, If, loops

# temp = 18

# if temp > 30:
#     print("Det är supervarmt")
# elif 20 <= temp <= 30:
#     print("Det är lagom varmt.")
# else:
#     print("Det är kallt")

# credit_score = 650

# status = "Godkänd för lån" if credit_score > 700 else "Du får inte låna"
# print(status)

# users = [("Bobbo", "Linköping"), ("Stefan", "Göteborg"), ("Charles", "Stockholm")]

# for name, city in users:
#     print(f"{name} bor i {city}")

# while True:
#     choice= input("Välj något i menyn")
#     if choice == "1":
#         break

# attempts = 0
# password = "123"

# while attempts < 3:
#     user_input = input("Ange lösenord: ")
#     if user_input == password:
#         print("Du är inloggad")
#         break
#     attempts += 1
# else:
#     print("För många försök")

# with open("example.txt", "w") as file:
#     file.write("Test \n test2 \n test3")

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "r") as file:
#     for line in file:
#         print(line, end="")

# list comprehension enumerate, Zip, In, Input, functions

# numbers = [1,2,3,4,5]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)

# print(squares)

# squares = [num ** 2 for num in numbers]
# print(squares)

# tools = ["Hammer", "Wrench", "Screwdriver"]
# for index, tool in enumerate(tools, start=1):
#     print(f"Tool #{index}: {tool}")

# names = ["Bobbo", "Guy", "Charlie"]
# car = ["Volvo", "Nissan", "Tesla"]

# for name, car in zip(names, car):
#     print(f"{name} har denna bil: {car}")

# colors = ["red", "blue", "green"]
# print("yellow" in colors)
# print("green" in colors)

# scores = [55, 35, 135, 32]
# print(f"Highest score {max(scores)}")
# print(f"Lowest scores: {min(scores)}")

# import random
# print(random.randint(1,100))

# colors = ["red", "blue", "green"]
# print(random.choice(colors))

def greet(name="Okänd"):
    return f"Hello {name}"

print(greet("Bobbo"))