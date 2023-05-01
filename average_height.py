# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
num_students = 0

for average_height in student_heights:
    total_height += average_height
    num_students += 1
    
average_height = round(total_height / num_students)

print(f"The average height is {average_height}")

#for loop without sum() or len()





