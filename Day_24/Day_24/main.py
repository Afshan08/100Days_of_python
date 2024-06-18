#
# with open("name.txt") as file:
#     content = file.read()
#     print(content)

with open("name.txt", mode="w") as file:
    file.write("New text.")

with open("name.txt", mode="r") as file:
    print(file.read())

