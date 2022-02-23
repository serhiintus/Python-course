#class Student presents information about the student's success in the Python course
class Student(object):
    #constructor gets a string - the student's name and a dictionary containing the course settings
    def __init__(self, n_s, conf):
        self.name_student = n_s
        keys = conf.keys()
        if 'exam_max' in keys:
            self.exam_max = conf['exam_max']
        if 'lab_max' in keys:
            self.lab_max = conf['lab_max']
        if 'lab_num' in keys:
            self.lab_num = conf['lab_num']
        if 'k' in keys:
            self.k = conf['k']
        self.lab_list = [0 for i in range(self.lab_num)]
        self.exam = 0
    #this method gets 2 arguments, first is the number of points scored for the task (integer or real number), 
    #second is the non-negative integer, task ordinal
    def make_lab(self, m, n = None):
        if m > self.lab_max:
            m = self.lab_max
        if n == None:
            if 0 in self.lab_list:
                i = self.lab_list.index(0)
                self.lab_list[i] = m
                return self
            else:
                return self
        if n > (self.lab_num - 1):
            return self
        self.lab_list[n] = m
        return self
    #this method gets 1 argument is the integer or real number, grade for the final exam
    def make_exam(self, m):
        if m > self.exam_max:
            self.exam = self.exam_max
        else:
            self.exam = m
        return self
    #this method returns a tuple containing the real number (the sum of the student's points for the course) 
    #and the logical value True or False, depending on whether these points are enough to obtain a certificate
    def is_certified(self):
        points = sum(self.lab_list) + self.exam
        course_complete = False
        if points >= (self.k * 100):
            course_complete = True
            return (points, course_complete)
        else:
            return (points, course_complete)

#EXAMPLES:
conf = {
'exam_max': 30, #number of points for passing the exam
'lab_max': 7, #number of points for 1 practical work
'lab_num': 10, #number of practical works on the course
'k': 0.61, #the percentage of points from the maximum that must be scored to obtain a certificate
}
oleg = Student('Oleg', conf)
oleg.make_lab(1)  # labs: 1 0 0 0 0 0 0 0 0 0, exam: 0
print(oleg.lab_list, oleg.exam)
oleg.make_lab(8,0) # labs: 7 0 0 0 0 0 0 0 0 0, exam: 0
print(oleg.lab_list, oleg.exam)
oleg.make_lab(1)  # labs: 7 1 0 0 0 0 0 0 0 0, exam: 0
print(oleg.lab_list, oleg.exam)
oleg.make_lab(10,7)  # labs: 7 1 0 0 0 0 0 7 0 0, exam: 0
print(oleg.lab_list, oleg.exam)
oleg.make_lab(4,1)  # labs: 7 4 0 0 0 0 0 7 0 0, exam: 0
print(oleg.lab_list, oleg.exam)
oleg.make_lab(5)  # labs: 7 4 5 0 0 0 0 7 0 0, exam: 0
print(oleg.lab_list, oleg.exam)
oleg.make_lab(6.5) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 0
print(oleg.lab_list, oleg.exam)
oleg.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.lab_list, oleg.exam)
print (oleg.is_certified()) # (59.5, False)
oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.lab_list, oleg.exam)
print (oleg.is_certified()) # (62.5, True)