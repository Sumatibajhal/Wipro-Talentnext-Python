'''
'''
from collections import Counter
import re

def find_meeting_details(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    num_lines = len(lines)
    if num_lines <= 12:
        meeting_time = f"{num_lines} AM"
    else:
        hour = num_lines % 12
        hour = 12 if hour == 0 else hour
        meeting_time = f"{hour} PM"
    all_text = ' '.join(lines)
    words = re.findall(r'\b\w+\b', all_text) 
    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]

    meeting_place = f"{most_common_word} Street"

    return f"Meeting time: {meeting_time}\nMeeting place: {meeting_place}"
