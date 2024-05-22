from typing import List

class Solution:
    def justify_text(self, words, max_width, is_last_line=False):
        
        if is_last_line or len(words) == 1:
            return ' '.join(words).ljust(max_width)
        
        total_spaces = max_width - sum(len(word) for word in words)
        num_gaps = len(words) - 1
        
        base_spaces = total_spaces // num_gaps
        extra_spaces = total_spaces % num_gaps
        
        justified_text = ''
        for i in range(len(words) - 1):
            justified_text += words[i] + ' ' * (base_spaces + (1 if i < extra_spaces else 0))
        
        justified_text += words[-1]
        
        return justified_text
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_length = 0
        line_word = []
        
        for word in words:
            if (line_length + len(line_word) + len(word)) > maxWidth:
                result.append(line_word)
                line_length = len(word)
                line_word = [word]
            else:
                line_length += len(word)
                line_word.append(word)
                
        if line_word:
            result.append(line_word)
        
        for index, line in enumerate(result):
            result[index] = self.justify_text(line, maxWidth)
            
        return result
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    justified_text = sol.fullJustify(words, maxWidth)
    # for line in justified_text:
    #     print(line)
        
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    justified_text = sol.fullJustify(words, 20)
    for line in justified_text:
        print(line)