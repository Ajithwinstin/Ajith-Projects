Problem Statement: Write a program to build a simple Student Management System using Python which can perform the following operations:

1. Accept
2. Display
3. Search
4. Delete
5. Update


Accept – This method takes details from the user like name, roll number, and marks for two different subjects.
# Method to enter new student details
def accept(self, Name, Rollno, marks1, marks2 ):
    # Creates a new class constructor
    # and pass the details
    ob = Student(Name, Rollno, marks1, marks2 )

    # list containing objects of student class
    ls.append(ob)

Display – This method displays the details of every student.
# Function to display student details     
def display(self, ob):
    print("Name   : ", ob.name)
    print("RollNo : ", ob.rollno)
    print("Marks1 : ", ob.m1)
    print("Marks2 : ", ob.m2)
    print("\n")    


Search – This method searches for a particular student from the list of students. This method will ask the user for roll number and then search according to the roll number
# Search Function    
def search(self, rn):
    for i in range(ls.__len__()):
        # iterate through the list containing
        # student object and checks through
        # roll no of each object
        if(ls[i].rollno == rn):
            # returns the object with matching 
            # roll number
            return i 

Delete – This method deletes the record of a particular student with a matching roll number.
# Delete Function                                  
def delete(self, rn):
    # Calls the search function 
    # created above
    i = obj.search(rn)  
    del ls[i]


Update – This method updates the roll number of the student. This method will ask for the old roll number and new roll number. It will replace the old roll number with a new roll number.
# Update Function   
def update(self, rn, No):
    # calling the search function
    # of student class
    i = obj.search(rn)
    ls[i].rollno = No
