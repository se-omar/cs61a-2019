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
    if not word1: # Fill in the condition
        # BEGIN Q6
        return len(word2)
        # END Q6

    elif not word2: # Feel free to remove or add additional cases
        # BEGIN Q6
        return len(word1)
        # END Q6

    elif word1[0] == word2[0]:
        return score_function(word1[1:], word2[1:])

    else:
        add_char = score_function(word1, word2[1:])  # Fill in these lines
        remove_char = score_function(word1[1:], word2)
        substitute_char = score_function(word1[1:], word2[1:])
        # BEGIN Q6
        return  1 + min(add_char, remove_char, substitute_char)
        # END Q6

def score_function_accurate(word1, word2):
    if not word1: # Fill in the condition
        # BEGIN Q6
        return float(len(word2))
        # END Q6

    elif not word2: # Feel free to remove or add additional cases
        # BEGIN Q6
        return float(len(word1))
        # END Q6

    elif word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])

    else:
        add_char = 1.0 + score_function(word1, word2[1:])  # Fill in these lines
        remove_char = 1.0 + score_function(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word1[0], word2[0]] + score_function(word1[1:], word2[1:])
        # BEGIN Q6
        return  min(add_char, remove_char, substitute_char)
        # END Q6
KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
def score_function_final(word1, word2):
    def helper(word1, word2, word_memo={}):
        if (word1, word2) in word_memo: 
            return word_memo[word1, word2]
        if (word2, word1) in word_memo:
            return word_memo[word2, word1]

        if word1 == word2:
            return float(0)

        if not word1: # Fill in the condition
            # BEGIN Q6
            return float(len(word2))
            # END Q6

        elif not word2: # Feel free to remove or add additional cases
            # BEGIN Q6
            return float(len(word1))
            # END Q6

        elif word1[0] == word2[0]:
            return helper(word1[1:], word2[1:], word_memo)

        else:
            add_char = 1.0 + helper(word1, word2[1:], word_memo)  # Fill in these lines
            remove_char = 1.0 + helper(word1[1:], word2, word_memo)
            substitute_char = KEY_DISTANCES[word1[0], word2[0]] + helper(word1[1:], word2[1:], word_memo)
            curr_score = min(add_char, remove_char, substitute_char)
            word_memo[word1, word2] = curr_score
            return curr_score
    return helper(word1, word2)
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

def swap_score(s1, s2):
    if not s1 or not s2:
        return 0
    elif s1[0] != s2[0]:
            return 1 + swap_score(s1[1:], s2[1:])
    else:
        return swap_score(s1[1:], s2[1:])







