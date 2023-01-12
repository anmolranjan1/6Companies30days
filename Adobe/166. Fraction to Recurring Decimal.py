class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator//denominator)
        sign = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res = sign + str(numerator//denominator) + '.'
        numerator %= denominator
        i, p = 0, ''
        m = {numerator:i}
        while numerator % denominator:
            numerator *= 10
            i += 1
            r = numerator % denominator
            p += str(numerator // denominator)
            if r in m:
                p = p[:m[r]]+'('+p[m[r]:]+')'
                return res + p
            m[r] = i
            numerator = r
        return res + p