correct_criminalname = "dany"
correct_criminalnumber= "420"
criminalname = input("Enter criminal name: ").lower()
criminalnumber = input("Enter  criminal number: ")
if criminalname == correct_criminalname and criminalnumber == correct_criminalnumber:
    print("Criminal found in the police station list.")
else:
    print("Criminal not found in the police station list.")
