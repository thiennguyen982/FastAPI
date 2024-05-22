def intToRoman(num: int) -> str:
    symbol_value_map = {'I': 1,
                        'IV': 4,
                        'V': 5,
                        'IX': 9,
                        'X': 10,
                        'XL': 40,
                        'L': 50,
                        'XC': 90,
                        'C': 100,
                        'CD': 400,
                        'D': 500,
                        'CM': 900,
                        'M': 1000
                        }
    result = ""
    for key, value in sorted(symbol_value_map.items(), key=lambda x: x[1], reverse=True):
        while num >= value:
            result += key
            num -= value
    return result

if __name__ == "__main__":
    print(intToRoman(123))