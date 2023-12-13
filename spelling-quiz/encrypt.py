import random
import itertools
import os

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]

alphabet = list('abcdefghijklmnopqrstuvwxyz')



# Does it shuffle every time or just once?
# random.shuffle(shuffled := alphabet[:])
# It does it every Time
# dictionary = dict(zip(alphabet, shuffled))

# I think i have to do brute force until I find the Alphabet correlation

# Generate all possible combinations
# n = len(alphabet)
# combinations = []
# for r in range(1, n + 1):
#     combinations.extend(itertools.combinations(alphabet, r))

# # Print the combinations
# all_combinations = []
# for combo in combinations:
#     all_combinations.append(''.join(combo))
    
# print(all_combinations)
    

random.shuffle(shuffled := alphabet[:])
dictionary = dict(zip(alphabet, shuffled))

for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    # print(encrypted)
    open(filename, 'w').write(encrypted)
