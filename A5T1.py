results={"Akshat":80,"Brian":60,"Dia":85,"Daniel":90,"Freya":78,"Keth":91}
inpt=input("Enter the student's name:").capitalize()


if inpt.isnumeric():
    print("Entered name is invalid,Please enter the student name again:")
    inpt = input().capitalize()


if inpt in results:
   print(inpt,"'s marks:",results[inpt])
else:
   print("Student not found.")




