#Program to determine Student Grade By Inputing the Marks
# subject_mark is the input by student
def mark_grade():

    subject_mark = int(input("What is your Mark In Percentage?:"))
    if  100 > subject_mark >= 70:
        output = "You scored a GRADE A"
    elif 70 > subject_mark >= 60:
        output = "You scored a GRADE B"
    elif 60 > subject_mark >= 50: 
        output = "You scored a GRADE C"
    elif 50 > subject_mark >= 40:
        output = "You scored a GRADE D"
    elif subject_mark < 40:
        output = "You scored a GRADE E"
    else:
        output = "You have entered an Incorrect Mark"

# This is how far i could go on the 2nd part of the question.
    #for A in range(70, 101):
    #    for B in range(60, 70):
    ###              if int(target_grade) > subject_mark:
       #                 output = "You need to do better next time "
        #            if int(target_grade) ==  subject_mark:
         #               output = "You were bang on target "
          #          if int(target_grade) < subject_mark:
           #             output = "You have done very well. "
    #else:
     #  output = "Wrong Entry For input Options"

    return output

student_grade = mark_grade()
print(student_grade)