# Class List Manager - Group1
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = ["Renad", "Rawan", "Joud", "Reema", "Yara"]
# ===== Each student adds her function BELOW this line =====
#written by: Renad (task 1)
def count_names(names):
    return len(names)
#written by:Rawan (task 2)
def search_name(names, name):
    return name in names
# Written by: Joud (task 8)
def remove_duplicates(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    print("Number of names:", count_names(names))
    print("Search result:", search_name(names, "Rawan"))
    print("List without duplicates:", remove_duplicates(names))

main()
# Written by: Yara (Task 7)
def count_vowels(name):
    count = 0
    for letter in name.lower():
        if letter in "aeiou":
            count += 1
    return count

print("Number of vowels:", count_vowels(names[0]))

main
