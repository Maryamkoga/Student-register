#Input for the number of students registering to be entered
num_students = int(input("Enter the number of students registering: "))

#List to store registered students ID
stud_registered = []

#The student id entered is written to a text file called reg_form
with open("reg_form.txt", "w", encoding = "utf-8") as file:
    #Variable entry_number is created so the student id is numbered when written to text file
    entry_number = 1  
    #While loop created to ensure number of students to register equals number of student ID entered
    while len(stud_registered) < num_students:
        #User input is created for student id number to be entered
        id_student = input("Enter student ID number: ")
        #If statement to ensure student id is entered only once
        #Print statement shows student ID that has been entered
        if id_student in stud_registered:
            print(f"Student with ID {id_student} is already registered.")
        else :
            stud_registered.append(id_student) #to add student id entered to the list
    #To sort the student id stored in the list in order, that way it is easier to use as an attendance list
    stud_registered.sort()
    for id_student in stud_registered:
        file.write(f"{entry_number}. {id_student}\n")
        #A dotted line is also created for students to sign under their respective ID number
        file.write("--------------------------\n")
        file.write("\n") #for extra space 
        #Entry number increases for every student entered
        entry_number += 1
#The loop ends when the last student is registered
#The file will be closed automatically here
#if the file needs to be closed explicitly after the with statement 
file.close() 



