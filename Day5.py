# Lecture 38 😁/////////////////////////////////
# Using for loop with Python List
fruits =["apple","peach","pear"]

for index in fruits:
    print(index)
    print(index + " pie")

print(index)


# Lecture 39 😁/////////////////////////////////////
# Highest Score

student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]
total_exam_score = sum(student_scores)# sum is a built in function which is use to add
sum = 0

for score in student_scores:
    sum += score

print(sum)

print(total_exam_score)

# Max built in Keyword
print(max(student_scores))



