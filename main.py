# this is our SCRIPT!!
import grade_utils # bringing in as a module

# step 1: define our class data
class_data = {
    'Alice Nguyen': [92, 88, 95, 91, 97],
    'Bob Martinez': [74, 68, 72, 80, 65],
    'Carol Smith': [55, 60, 58, 62, 50],
    'David Kim': [85, 89, 91, 88, 94],
    'Eva Johnson': [78, 82, 76, 80, 83],
    'Frank Lee': [95, 98, 100, 96, 99],
    'Grade Patel': [63, 70, 66, 68, 72],
    'Henry Thompson': [88, 85, 90, 87, 92]
}

# create a class grade report
print('Class Grade report:')
results = grade_utils.summarize_class(class_data)
#print(results)

# class statistics
print('Class statistics:')
stats = grade_utils.class_statistics(results)

print('Class Average:', stats['class_avg'])
print('High score:', stats['highest'])
print('Low score:', stats['lowest'])

# find top students (default threshold of 0.90)
top_students = grade_utils.find_top_students(results)

print('Top students with a 90+:')
if top_students:
    for student in top_students:
        print(f'{student['name']:<20} avg: {student['average']:.2f}')
else:
    print('No students met the criteria.')
    
# flag students who need attention (< 70)
struggling = grade_utils.find_top_students(results, threshold=0.0)
struggling = [s for s in results if s['average'] < 70.0] # filter

print('\nStudents who are below 70:')
if struggling:
    for student in struggling:
        print(f'{student['name']:<20} avg: {student['average']:.2f}')
else:
    print('All students are at 70 or above.')