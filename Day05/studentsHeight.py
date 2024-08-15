student_list = input().split()

for n in range(0,len(student_list)):
   student_list[n] = int(student_list[n]) 
 
total_Height = 0
for height in student_list:
   total_Height += height
   
print(f"total height is :{total_Height}")

Total_students = 0
for students in student_list:
   Total_students += 1

print(f"total number of students {Total_students}")

average_height = int(total_Height / Total_students)
print(average_height)