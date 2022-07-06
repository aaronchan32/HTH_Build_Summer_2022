full_name = "Aaron Chan"
favorite_nickname = "AAron"
age = 19
python_experience = True

favorite_hobbies = [
    "playing video games", "rock climbing", "reading manga", "watching anime"
]

favorite_things = {
    "movie": "Everything Everywhere All at Once",
    "food": "Pandan Waffle",
    "hobby": favorite_hobbies[1],
    "video game": "League of Legends"
}

print(full_name, favorite_nickname, age, python_experience, "\n")

print(favorite_hobbies, "\n")

print(favorite_things)

# Python's print function = Java's print function: System.out.println();

# print(full_name, favorite_nickname, age, python_experience)
# print() #the print function adds a new empty line when no args are provided
# print(favorite_hobbies)
# print()
# print(favorite_things)

all_vars = dict(vars())
