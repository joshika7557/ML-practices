import numpy as np
marks = np.array([78, 85, 92, 67, 88, 95, 72])
print("Marks:", marks)
print("Average:", np.mean(marks))
updated_marks = marks + 5
print("Updated Marks:", updated_marks)
high_scores = marks[marks > 80]
print("Marks above 80:", high_scores)
sorted_marks = np.sort(marks)
print("Sorted Marks:", sorted_marks)