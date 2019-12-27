class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            result_len = len(a) + 1
        else:
            a, b = b, a
            print(a,b)
            result_len = len(a) + 1
            print(result_len)
        a_len = len(a)
        b_len = len(b)
        print(a_len, b_len)
        result = ''
        add = False
        for i in range(result_len):
            if i < b_len:
                if add:
                    if (a[a_len - i - 1] == '1') and (b[b_len - i - 1] == '1'):
                        result = '1' + result
                    elif (a[a_len - i - 1] == '1') and (b[b_len - i - 1] == '0'):
                        result = '0' + result
                    elif (a[a_len - i - 1] == '0') and (b[b_len - i - 1] == '1'):
                        result = '0' + result
                    elif (a[a_len - i - 1] == '0') and (b[b_len - i - 1] == '0'):
                        result = '1' + result
                        add = False
                else:
                    if (a[a_len - i - 1] == '1') and (b[b_len - i - 1] == '1'):
                        result = '0' + result
                        add = True
                    elif (a[a_len - i - 1] == '1') and (b[b_len - i - 1] == '0'):
                        result = '1' + result
                    elif (a[a_len - i - 1] == '0') and (b[b_len - i - 1] == '1'):
                        result = '1' + result
                    elif (a[a_len - i - 1] == '0') and (b[b_len - i - 1] == '0'):
                        result = '0' + result
                
                print(result)
            elif i < a_len:
                if add:
                    if a[a_len - i - 1] == '1':
                        result = '0' + result
                    else:
                        result = '1' + result
                        add = False
                else:
                    result = a[a_len - i - 1] + result
                print(result)
            elif i == a_len:
                if add:
                    result = '1' + result
                print(result)
        return result