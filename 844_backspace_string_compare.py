class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def calc_c(string):
            stack = 0 #counting how many times # stack in row
            c = "" #here we will store modified string

            #we want to go from behind the string
            #so the "#" can imitate backspace
            for i in range(len(string)-1,-1, -1):
                #if character is "#" just add one to the stack
                if string[i] == "#":
                    stack +=1
                
                #if char is not "#", check if there is any in stack
                #if there is none in stack then save the letter
                else:
                    if stack <=0:
                        c += string[i]
                    #if there is something left in stack
                    # then skip/delete the char
                    else:
                        stack-=1
            return c
        
        t = calc_c(t)
        s = calc_c(s)
        #compare if t is equal to s after processing
        if t == s: return True
        else: return False


# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

