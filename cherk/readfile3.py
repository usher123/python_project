def readfile(gradefile):
    '''(file open for reading)->dict of {float:list of str}
    read the grades from gradefile anf teturn a dictionary'''

    line = gradefile.readline()

    grade_to_ids = {}
    b=line.split(' ')
    while line != '':
        for int in range(0,len(b)-1,2):
            student_id =b[int]
            grade = float(b[int+1])
        
            if grade not in grade_to_ids:
                 grade_to_ids[grade] = [student_id]
            else:
                 grade_to_ids[grade].append(student_id)
       
        line = gradefile.readline()
        b=line.split(' ')
    
    return  grade_to_ids

if __name__ == '__main__':
    gradefile = open('/home/zhangpeng/github/python_project/text/record')
    print(readfile(gradefile))


