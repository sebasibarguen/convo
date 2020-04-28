import string
from collections import defaultdict
from itertools import permutations



def permutate_word(word: str, distance: int = 1):
    """
    From a given word, returns all permutations of that word, that are :distance: apart.
    """
    letter_groups = (''.join(p) for p in permutations(string.ascii_lowercase, distance))
    # Convert to list, faster to permute.
    word_list = [c for c in word]
    # Create permutation set
    word_permutations = set()

    d = distance
    for i in range(len(word_list)):
        for chars in letter_groups:
            insert = ''.join(word_list[:i]) + chars + ''.join(word_list[i:])
            delete = ''.join(word_list[:i] + word_list[i+d:])
            substitute = ''.join(word_list[:i]) + chars + ''.join(word_list[i+d:])

            # Add permutations
            word_permutations.update( [insert, substitute, delete] )

    # Padded letters. Before and after.
    for chars in letter_groups:
        pre = chars + word
        pos = word + chars
        word_permutations.update( [pre, pos] )

    return word_permutations


def match(keyword: str, word_dict: dict, suggestions: int = 10, weight: str = 'simple') -> list:
    """
    Matches keyword 
    """
    matches = []

    if keyword in word_dict:
        matches.append( (0, keyword) )

    distance = 0
    while len(matches) < suggestions:
        distance += 1

        permutations = permutate_word(keyword, distance)
        for word in permutations:
            if word in word_dict:
                # Set score
                if weight == 'simple':
                    score = distance
                elif weight == 'frequency':
                    score = word_dict[word]
                elif weight == 'mixed':
                    score = (1/distance) * word_dict[word]

                matches.append( (score, word) ) 

    matches.sort(reverse = True)
    return matches[:suggestions]