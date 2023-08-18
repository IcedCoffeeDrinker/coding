
print(2**3)                # 2 hoch 3

def raise_to_power(base_num, pow_num):             # 3 hoch 4 in kompliziert warum auch immer
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return  result
print(raise_to_power(3, 4))