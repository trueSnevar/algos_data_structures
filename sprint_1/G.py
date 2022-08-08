def get_sum(first_number: str, second_number: str) -> str:
    res = ''
    carry = ''
    for i in range(len(first_number)-1, -1, -1):
        if (first_number[i] == '1' and second_number[i] == '1'):
            res += '0'
            if not carry:
                carry += '1'
        elif (first_number[i] == '0' and second_number[i] == '0'):
            if not carry:
                res += '0'
            else:
                res += '1'
                carry = ''    
        else:
            if not carry:
                res += '1'
            else:
                res += '0'

    if carry:
        res += carry

    return res[::-1]

print(get_sum('1010', '1011')) # 10101
print(get_sum('1', '1')) # 10