'''
Project 2:
Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score. You have scores. Store them in a list and find the score of the runner-up.
'''

scores = [2, 3, 6, 6, 5]

unq_scores = sorted(set(scores), reverse=True)

runner_up = unq_scores[1]

print("Runner-up score:", runner_up)
