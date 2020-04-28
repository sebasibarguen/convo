import os

from fuzzy_match import word_permutations


class FuzzyMatcher:
    """
    A class to a matcher.

    ...

    Attributes
    ----------
    word_file_path : str
        File path to use to build up the word dictionary
    algorithm : str
        Algoritthm to use for fuzzy match

    Methods
    -------
    match(keyword="", suggestions=10):
        Matches the <keyword> and returns a list of #<suggestions>
    """

    def __init__(self, algorithm='word_permutations', word_file_path=None):

        if word_file_path is None:
            dir_name = os.path.dirname(os.path.realpath(__file__))
            word_file_path = os.path.join(dir_name, 'data', 'count_1w.txt')

        self.word_dict = {}
        self.algorithm = algorithm
        self.file_path = word_file_path

        # Build dictionary
        self.build_word_dict()


    def build_word_dict(self):
        """
        Build the word dictionary from the file path. The key is the word, and the value is the
        word frequency.
        """

        line_gen = (line.rstrip().lower() for line in open(self.file_path, 'r'))
        max_freq = 0
        for line in line_gen:
            word, freq = line.split()
            freq = int(freq)
            self.word_dict[word] = freq

            max_freq = max(max_freq, freq)
        
        for word, freq in self.word_dict.items():
            self.word_dict[word] = freq / max_freq

    
    def match(self, keyword: str, suggestions: int = 10, weight: str = 'mixed') -> list:
        """
        From a given keyword, return a list of suggestions.

        Parameters:
            keyword (str): Keyword to do fuzzy match on
            suggestions (int): Number of suggestions

        Returns:
            suggestions (list): List of suggestions
        """

        if weight not in ['simple', 'frequency', 'mixed']:
            raise ValueError(':weight: parameter must be either: simple, frequency or mixed')

        matches = []
        if self.algorithm == 'word_permutations':
            matches = word_permutations.match(keyword, self.word_dict, suggestions, weight)

        return matches
