import sys


class HoneycombSolver:
    MIN_WORD_LENGTH = 4

    def __init__(self, required_char, valid_chars, wordlist):
        self.required_char = required_char.lower()
        self.valid_chars = set(valid_chars.lower())
        self.wordlist = wordlist

    def solve(self):
        matches = []

        with open(self.wordlist, 'r') as lines:
            for line in lines:
                word = line.strip().lower()

                if (len(word) >= self.MIN_WORD_LENGTH and
                    self.required_char in word and
                    set(word.replace(self.required_char, '')).issubset(self.valid_chars)):

                    matches.append(word)

        return matches


if __name__ == '__main__':
    num_args = len(sys.argv)

    if num_args < 3:
        print('Usage: honeycomb_solver.py <required_char> <valid_chars> [wordlist]')
        sys.exit(1)

    wordlist = sys.argv[3] if num_args > 3 else 'wordlist.txt'
    hc = HoneycombSolver(sys.argv[1], sys.argv[2], wordlist)

    try:
        print('\n'.join(hc.solve()))
    except FileNotFoundError as e:
        print(e)
