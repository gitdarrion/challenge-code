example = "bobwatersracecar"

def isPalindrome(word):
    for i in range(0,len(word)):
        if not (word[i]==word[len(word)-1-i]):
            return False
    return True

def isPalindromes(word):
    
    palindromes = []
    left_break = 0
    right_break = len(word)-1 

    # Repeat until the left break is at the last index.
    while left_break < (len(word)-1): 

        # Converge left break and right break.
        while right_break > left_break: 

            # Extract the substring. 
            phrase = word[left_break:right_break+1]

            # Check with the simple palindrome function.
            is_palindrome_in_word = isPalindrome(phrase)

            # If the substring is a palindrome, add it to the list of palindromes.
            if is_palindrome_in_word:
                palindromes = palindromes + [phrase]
            
            # Shift the right break by 1 to the left.
            right_break -= 1 
        
        # Shift the left break by 1 to the right.
        left_break += 1

        # Reset the right break to the end of the word.
        right_break = len(word)-1

    # Return the list of palindromes.
    return palindromes 
        

    
palindromes = isPalindromes(example)
print palindromes