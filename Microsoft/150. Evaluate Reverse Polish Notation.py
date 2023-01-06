class Solution(object):
    def evalRPN(self, tokens):
        stack, d = [], {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':lambda x,y:int(float(x)/y)}
        for s in tokens:
            stack.append(d[s](*[stack.pop(), stack.pop()][::-1]) if s in d else int(s))
        return stack[-1]