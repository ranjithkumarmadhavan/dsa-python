class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        max_index_of_each_letter = {}

        index = 0
        for letter in s:
            max_index_of_each_letter[letter] = index
            index += 1
        
        print(max_index_of_each_letter)

        stack = []
        current_index = 0
        for letter in s:
            while letter not in stack and len(stack) > 0 and min(letter,stack[-1]) == letter and max_index_of_each_letter[stack[-1]] > current_index:
                stack.pop()

            if letter not in stack:
                stack.append(letter)
            current_index += 1
        result = ''
        for i in stack:
            result += i
        print(result)
        return result


s = Solution()
s.removeDuplicateLetters("abacb")