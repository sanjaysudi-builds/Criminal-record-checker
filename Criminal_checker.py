def find_criminal(name, number):
    criminal_records = {
        "dany": "420",
        "alex": "133",
        "john": "007"
    }
    return criminal_records.get(name) == number


name = input("Enter criminal name: ").strip().lower()
number = input("Enter criminal number: ").strip()

if find_criminal(name, number):
    print("Criminal found in the police station list.")
else:
    print("Criminal not found in the police station list.")
