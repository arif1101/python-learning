class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"Full Name: {self.firstname} {self.lastname}")

    def job(self, jobTitle, jobSalary):
        self.jobTitle = jobTitle
        self.jobSalary = jobSalary

    def printJobInfo(self):
        if hasattr(self, 'jobTitle') and hasattr(self, 'jobSalary'):
            print(f"Job: {self.jobTitle}")
            print(f"Salary: {self.jobSalary}")
        else:
            print("Job information not set.")

# Inherit from Person
class Student(Person):
    def __init__(self, fname, lname, graduationYear):
        super().__init__(fname, lname)
        self.graduationYear = graduationYear

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationYear}!")

    def fullProfile(self):
        print("--- Student Profile ---")
        self.printname()
        self.printJobInfo()
        print(f"Graduation Year: {self.graduationYear}")


# Create a Student instance
x = Student('Arif', 'Rahman', 2025)
x.printJobInfo()

# Set the job info first
x.job('Software Engineer', '100,000')

# Now print full profile
x.fullProfile()
