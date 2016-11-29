def most_classes(teachers):
    count =0
    teacherMC=""
    for teach in teachers:
        if len(teachers[teach]) > count:
           count = len(teachers[teach])
       	   teacherMC = teach 
            
    return teacherMC


def num_teachers(teachers):
    return len(teachers)

#def stats(teachers):
 #   teacher_list = []
  #  for teach in teachers:
   #     for val in teachers.values():
    #        teacher_list= [teach, val]
            
            
def courses(course_list):
    newList = []
    for k,v in dict.items():
        newString = [k, int(len(v))]
        newList.append(newString)

    return newList          

def stats(dict):
    newList = []
    for k in dict.values():
        newList = k
    return newList         


def most_classes(teachers):
    count =0
    teacherMC=""
    for teach in teachers:
        if len(teachers[teach]) > count:
           count = len(teachers[teach])
       	   teacherMC = teach 
            
    return teacherMC

def num_teachers(teachers):
    return len(teachers)

 
def courses(course_list):
    newList = []
    for k,v in dict.items():
        newString = [k, int(len(v))]
        newList.append(newString)
    return newList   