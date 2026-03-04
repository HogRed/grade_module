# custom module for processing student data

def compute_average(score):
    '''Calculates the average of a list of scores.
        Params:
            scores (list of float / int)
        
        Returns:
            float: average score (or 0.0 if list is empty)
        
        Example:
            compute_average([80,90,70]) --> 80.0
    '''
    if not score:
        return 0.0
    
    return sum(score) / len(score)
    
def letter_grade(average: float) -> str:
    '''Convert numeric average into a letter grade.
    
        Params:
            average (float)
        
        Returns:
            str: corresponding letter grade
        
        Example:
            letter_grade(93.5) --> "A"
    '''
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def summarize_class(class_data):
    '''Print a formatted grade summary for an entire class.
    
        Params:
            class_data (dict)
        
        Return:
            list of dict
        
        Example:
            input:
                {
                    'Alice': [88, 92, 79],
                    'Bob':   [70, 65, 73]
                }
    '''
    results = [] # to store student info
    
    print('\n' + '=' * 45)
    print(f'f{'STUDENT':<20} {'AVERAGE':>8} {'GRADE':>5}')
    print('='*45)
    # ==========================
    # STUDENT    AVERAGE   GRADE 
    # ==========================
    
    # loop over each student and get their list of scores
    for name, scores in class_data.items():
        avg = compute_average(scores)
        grade = letter_grade(avg)
        
        # print formatted row
        print(f'{name:<20} {avg:>8} {grade:>5}')
        
        # build a result dict and add it to the result
        # list
        results.append({
          'name': name,
          'average': avg,
          'grade': grade  
        })
        
    print("="*45)
    
    return results

def find_top_students(results, threshold = 90.0):
    '''Filter a result list to find students who scored
        at or above a threshold.
        
        Params:
            results (list of dict)
            threshold (float)
        
        Returns:
            list of dict of students who met the threshold
        
    '''
    top = [student for student in results if student['average'] >= threshold]
    
    return top

def class_statistics(results):
    '''Compute class-wide statistics from a results list.
    
        Params:
            results (list of dict)
        
        Returns:
            dict: contains class_avg, highest, lowest values
    '''
    averages = [student['average'] for student in results]
    
    return {
        'class_avg': compute_average(averages),
        'highest': max(averages),
        'lowest': min(averages)
    }
    
## module self-test
if __name__ == '__main__':
    print('Running grade_utils.py self-test...')
    
    # sanity check
    test_scores = [88, 72, 75, 95, 60]
    avg = compute_average(test_scores)
    
    # expect 78.0
    print(f'compute_average({test_scores}) = {avg}')
    
    print(f'letter_grade(95) = {letter_grade(95)}') # expect A
    print(f'letter_grade(82) = {letter_grade(82)}') # expect B
    print(f'letter_grade(55) = {letter_grade(55)}') # expect F