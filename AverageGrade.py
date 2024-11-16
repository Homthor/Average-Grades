grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny',
            'Bilbo',
            'Steve',
            'Khendrik',
            'Aaron'}


#print(grades)
#print(students)
print("")

tuple(students)
students = sorted(students)
# print(students)

avg_grade_book = {}
# print(grade_book)

avg_grades = grades
print(avg_grades)

avg_grade_book.update({students[0]: sum(avg_grades[0])/len(avg_grades[0]),
                       students[1]: sum(avg_grades[1])/len(avg_grades[1]),
                       students[2]: sum(avg_grades[2])/len(avg_grades[2]),
                       students[3]: sum(avg_grades[3])/len(avg_grades[3]),
                       students[4]: sum(avg_grades[4])/len(avg_grades[4])})
print(avg_grade_book)


