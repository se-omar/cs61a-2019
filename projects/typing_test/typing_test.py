""" Typing Test implementation """

from asyncio import current_task
from tracemalloc import start
from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6
    
    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________ 
        substitute_char = ______________ 
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8

def new_sample(path, i):
    lines = lines_from_file(path)
    return lines[i]

def lines_from_file(path):
    file = open(path)
    lines = []
    if readable(file):
        for line in readlines(file):
            lines.append(strip(line))
    close(file)
    return lines

def analyze(sample_paragraph, typed_string, start_time, end_time):
    delta_time = end_time - start_time
    pseudo_word_count = len(typed_string) / 5
    sample_words = sample_paragraph.strip().split()
    typed_words = typed_string.strip().split()
    correct_words = 0
    real_word_count = 0
    for sample_word, typed_word in zip(sample_words,typed_words):
        real_word_count += 1
        if sample_word == typed_word:
            correct_words += 1
    if len(typed_words) == 0:
        accuracy = 0.0
    else:
        accuracy = (correct_words / real_word_count) * 100

    return [pseudo_word_count / (delta_time/60), accuracy]

def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # if word[0] in vowels:
    #     return word + 'way'
    const_cluster = ''
    for chr in word:
        if chr in vowels:
            if const_cluster == '':
                return word + 'way'
            break
        const_cluster += chr

    return strip(word, chars=const_cluster) + const_cluster + 'ay'

def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    min_word = words_list[0]
    min_score = score_function(user_input, min_word)
    for word in words_list:
        curr_score = score_function(user_input, word)
        if curr_score < min_score:
            min_score = curr_score
            min_word = word

    return min_word








