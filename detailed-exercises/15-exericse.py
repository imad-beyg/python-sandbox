your_name, character = input("Enter your name and after comma a character:" ).split(",")
print(f"Characters in your name : {len(your_name)}")
print(f"The letter '{character.lower()}' appears {your_name.lower().count(character.lower())} times ")
