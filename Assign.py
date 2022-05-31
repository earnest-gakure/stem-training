class person :
    def __init__(self,name,date_of_birth,height,weight) :
        self.name=name
        self.dob= dob
        self.height =  height
        self.weight = weight
    def print_age(self):
        self.age=2022-self.dob
        print(f"you are{self.age} years old")
    def print_bmi(self)
        self.bmi=self.height/self.weight
        print(f"your bmi is {self.bmi}")
class student(person):
    def __init__(self,name,dod,weight,form,favourite_subject):
        super ().__init__
    
    def __init__(self, name,favourite_subject,form):
        self.name=name
        self.favourite_subject =favourite_subject
        self.form=form
    def details(self):
        print(f"my name is {self.name} my favourite subject is {self.favourite_subject} and am in form {self.form}")
student=student("chris","maths",2)
student.details()()
class teacher:
    def __init__(self, name, salary,subject_teaching):
        self.name=name
        self.salary = salary
        self.subject_teaching = subject_teaching
    def details(self):
     print(f"my name is {self.name} i teach {self.subject_teaching} and my salary is {self.salary}")
person3=teacher("janet",50000,"chem")
person3.details()