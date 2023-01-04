class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for x in tokens:
            if x not in ["+","-","/","*"]:
                stk.append(int(x))
            else:
                a = stk.pop(-1)
                b = stk.pop(-1)
                if x == "/":
                    stk.append(int(b/a))
                else:
                    stk.append(eval(f"{b}{x}{a}"))

        return stk[0]