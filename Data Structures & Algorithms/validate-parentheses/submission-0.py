class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for a in s:
            if a in closeToOpen:
                if stack and stack[-1] == closeToOpen[a]:
                    stack.pop()
                else:
                    return False
            else:
                 stack.append(a)

        return True if not stack else False