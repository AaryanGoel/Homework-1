# author: Aaryan Goel apg5720@psu.edu 
letter = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))


if letter == "A":
  GradeP = 4.0
elif letter == "A-":
  GradeP = 3.67
elif letter == "B+":
  GradeP = 3.33
elif letter == "B":
  GradeP = 3.00
elif letter == "B-":
  GradeP = 2.67
elif letter == "C+":
  GradeP = 2.33
elif letter == "C":
  GradeP = 2.0
elif letter == "D":
  GradeP = 1.0
elif letter == "F":
  GradeP = 0.0

GPA1 = GradeP
print(f"Grade point for course 1 is: " + + str(GPA1))
# 2
letter = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))


if letter == "A":
  GradeP = 4.0
elif letter == "A-":
  GradeP = 3.67
elif letter == "B+":
  GradeP = 3.33
elif letter == "B":
  GradeP = 3.00
elif letter == "B-":
  GradeP = 2.67
elif letter == "C+":
  GradeP = 2.33
elif letter == "C":
  GradeP = 2.0
elif letter == "D":
  GradeP = 1.0
elif letter == "F":
  GradeP = 0.0

GPA2 = GradeP
print(f"Grade point for course 2 is: " + str(GPA2))
#3
letter = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))


if letter == "A":
  GradeP = 4.0
elif letter == "A-":
  GradeP = 3.67
elif letter == "B+":
  GradeP = 3.33
elif letter == "B":
  GradeP = 3.00
elif letter == "B-":
  GradeP = 2.67
elif letter == "C+":
  GradeP = 2.33
elif letter == "C":
  GradeP = 2.0
elif letter == "D":
  GradeP = 1.0
elif letter == "F":
  GradeP = 0.0

GPA3 = GradeP
print(f"Grade point for course 3 is: " + str(GPA3))

GPAt = ((GPA1 * credit1) + (GPA2 * credit2) + (GPA3 * credit3)) / (credit1 + credit2 + credit3)
print(f"Your GPA is: {GPAt}" )
