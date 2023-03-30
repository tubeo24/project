class Student:

    def __init__(self):
        self.id = int(input('Hay nhap ID:'))
        self.name = input('Hay nhap ten SV:')
        self.grades = {}
        self.GPA = 0

    def print_info(self):
        print(f'student ID: {self.id}')
        print(f'student name: {self.name}')
        for subject in self.grades:
            print(f'{subject}: {self.grades[subject]}')
        print(f'student gpa: {self.gpa}')    

    def add_new_subject(self):
        so_mon_muon_nhap = int(input('Hay nhap so luong mon moi:'))
        for i in range(so_mon_muon_nhap):
            new_subject = input('hay nhap ten mon hoc moi:')
            self.grades[new_subject] = float(input(f'hay nhap diem cho mon hoc moi {new_subject}:'))

    def calculate_gpa(self):
        total = 0
        for subject in self.grades:
            total += self.grades[subject]
        self.gpa = total / len(self.grades)   
           
    def dieu_kien_tot_nghiep(self):
            if (self.gpa)/10*4 >= 2.5:
                print("Ban Da Du Dieu Kien Tot Nghiep" ) 
            else: 
                print("Ban da truot tot nghiep")

student_1 = Student()
student_1.add_new_subject()
student_1 .calculate_gpa()
student_1.print_info()
student_1.dieu_kien_tot_nghiep()