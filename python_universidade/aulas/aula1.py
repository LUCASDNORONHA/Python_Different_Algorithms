'''
Caculating average using a Python function.
'''

Score1 = float((input('\n Enter the value of your first grade: ')))
Score2 = float((input('\n Enter the value of your second grade: ')))
Score3 = float((input('\n Enter the value of your third grade: ')))

# Function AverageCalculator receive 3 parameters (a, b, c)
# Return average and status

def AverageCalculator (pScore1, pScore2, pScore3):
    m = (pScore1 + pScore2 + pScore3) /3
    if (m >= 7):
        return str(f'{m:.2f}') + ' - Approved '
    elif (m < 4):
        return str( f'{m:.2f}') + ' - Failed '
    else:
        return str( f'{m:.2f}') + ' - Exam '
    
print('\n The average of 3 grade is ', AverageCalculator(Score1, Score2, Score3))

'''
Status:

Approved if average >= 7
Failed if average < 4
Exame if average < 7 and average >= 4
'''