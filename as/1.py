# class CalcGCD:
#     def __init__(self, x, y):
#         self.x = self.processData(x)
#         self.y = self.processData(y)

#     def calculateGCD(self):
#         a, b = CalcGCD.myMax(self.x, self.y)
#         ans = self.calcGCD(a, b)
#         return self.resultFormat(ans)

#     def calcGCD(self, p_high, p_low):
#         if p_low == 0:
#             return p_high
        
#         rmd = p_high%p_low

#         a, b = CalcGCD.myMax(rmd, p_low)

#         return self.calcGCD(a, b)

#     def processData(self, data):
#         # Transform:    onetwo => 12
#         words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

#         ans = int(self.recursion(0, data, '', words))
#         return ans

#     def recursion(self, i, p_str, p_curr, p_words):
#         #Termination
#         if i == len(p_str):
#             if p_curr in list(p_words.keys()):
#                 return (p_words[p_curr])
#             else:
#                 return ''
    
#         #Conditional Calls
#         if p_curr in list(p_words.keys()):
#             return ((p_words[p_curr]) + self.recursion(i+1, p_str, p_str[i], p_words))
#         else:
#             return self.recursion(i+1, p_str, p_curr + p_str[i], p_words)
        
    
#     def resultFormat(self, p_data):
#         if p_data < 10:
#             return str(p_data)
        
#         return self.resultFormat(p_data//10) + str(p_data%10)
    
#     @staticmethod
#     def myMax(p_high, p_low) -> tuple:
#         a = 0
#         b = 0 
#         if p_high > p_low:
#             a = p_high
#             b = p_low
#         else:
#             b = p_high
#             a = p_low
        
#         return (a,b)
        
# obj = CalcGCD('eighteight', 'oneone')
# result = obj.calculateGCD()
# print(f'Result: {result}')


# class WordToNumberProcessor:
#     def __init__(self):
#         self.words = {
#             'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
#             'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
#         }
    
#     def processData(self, data):
#         return int(self._recursion(0, data, '', self.words))
    
#     def _recursion(self, i, p_str, p_curr, p_words):
#         if i == len(p_str):
#             return p_words.get(p_curr, '')
        
#         if p_curr in p_words:
#             return p_words[p_curr] + self._recursion(i + 1, p_str, p_str[i], p_words)
#         else:
#             return self._recursion(i + 1, p_str, p_curr + p_str[i], p_words)


# class GCDCalculator:
#     @staticmethod
#     def calcGCD(p_high, p_low):
#         if p_low == 0:
#             return p_high
#         rmd = p_high % p_low
#         a, b = MaxUtil.myMax(rmd, p_low)
#         return GCDCalculator.calcGCD(a, b)


# class MaxUtil:
#     @staticmethod
#     def myMax(p_high, p_low) -> tuple:
#         if p_high > p_low:
#             return p_high, p_low
#         else:
#             return p_low, p_high


# class CalcGCD:
#     def __init__(self, x, y):
#         self.processor = WordToNumberProcessor()
#         self.x = self.processor.processData(x)
#         self.y = self.processor.processData(y)

#     def calculateGCD(self):
#         a, b = MaxUtil.myMax(self.x, self.y)
#         ans = GCDCalculator.calcGCD(a, b)
#         return self._resultFormat(ans)

#     def _resultFormat(self, p_data):
#         if p_data < 10:
#             return str(p_data)
#         return self._resultFormat(p_data // 10) + str(p_data % 10)


# # Example Usage
# obj = CalcGCD('eighteight', 'oneone')
# result = obj.calculateGCD()
# print(f'Result: {result}')


class WordToNumberProcessor:
    def __init__(self):
        self.words = {
            'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }
    
    def processData(self, data):
        return int(self._recursion(0, data, '', self.words))
    
    def _recursion(self, i, p_str, p_curr, p_words):
        if i == len(p_str):
            return p_words.get(p_curr, '')
        
        if p_curr in p_words:
            return p_words[p_curr] + self._recursion(i + 1, p_str, p_str[i], p_words)
        else:
            return self._recursion(i + 1, p_str, p_curr + p_str[i], p_words)


class GCDCalculator:
    @staticmethod
    def calcGCD(p_high, p_low):
        if p_low == 0:
            return p_high
        rmd = p_high % p_low
        a, b = MaxUtil.myMax(rmd, p_low)
        return GCDCalculator.calcGCD(a, b)


class MaxUtil:
    @staticmethod
    def myMax(p_high, p_low) -> tuple:
        if p_high > p_low:
            return p_high, p_low
        else:
            return p_low, p_high


class NumberToWords:
    def __init__(self):
        self.num_to_words = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 
            90: 'ninety'
        }
    
    def numberToWords(self, num):
        if num < 0:
            return "negative " + self._convert(abs(num))
        return self._convert(num)
    
    def _convert(self, num):
        if num == 0:
            return self.num_to_words[0]
        
        if num < 10:
            return self.num_to_words[num]
        
        result = ""
        # Handle tens and ones separately
        if num >= 10 and num < 20:
            result = self.num_to_words[num]
        else:
            tens = (num // 10) * 10
            ones = num % 10
            result = self.num_to_words[tens]
            if ones > 0:
                result += self.num_to_words[ones]
        
        return result


class CalcGCD:
    def __init__(self, x, y):
        self.processor = WordToNumberProcessor()
        self.x = self.processor.processData(x)
        self.y = self.processor.processData(y)
        self.number_to_words = NumberToWords()

    def calculateGCD(self):
        a, b = MaxUtil.myMax(self.x, self.y)
        ans = GCDCalculator.calcGCD(a, b)
        return self.number_to_words.numberToWords(ans)


# Example Usage
obj = CalcGCD('eighteight', 'oneone')
result = obj.calculateGCD()
print(f'Result in words: {result}')
