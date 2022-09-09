import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week=9
print("Classes per week:", classes_per_week)
cost_per_class= (cost_per_week/classes_per_week)
print("This is your cost per class:", cost_per_class)

#Part B
my_grades=[92, 94, 80, 85, 90]
print(random.choice(my_grades))