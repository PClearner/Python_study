name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

language = ' python '
print(language+"kk")
language = language.rstrip()
print(language+"hh")

language = ' python '
print("dd"+language.lstrip())
print("mm"+language.strip()+"kk")

url = "https://nostarch.com"
print(url.removeprefix("https://"))

message = "set up a project call ' agent "
print(message)

#try
name = "Eric"
print(f"Hello {name},would you like to learn python?")

name = "Eric"
print(name.title())
print(name.upper())
print(name.lower())

name = "Albert"
print(f'{name} once say that "hello world!"')

name = "  \tllxxs  \n  "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())     #can cancel '\n \t'

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
