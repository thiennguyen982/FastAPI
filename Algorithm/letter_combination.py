class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        output = []
        for char in digits:
            if not output:
                output = digit_to_letters[char]
            else:
                new_output = []
                for str_ in output:
                    for letter in digit_to_letters[char]:
                        new_output.append(str_ + letter)
                output = new_output

        return output