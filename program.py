import sys


def arabic_to_roman(param):
    arab_to_rom = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    roman = []
    try:
        num = int(param)
        if num < 1 or num > 3999:
            raise ValueError("Roman numeral doesn't exist")
    except ValueError as e:
        raise e
    else:
        if num in arab_to_rom.keys():
            return arab_to_rom[num]

        for key, val in arab_to_rom.items():
            quotient, num = divmod(num, key)
            roman.append(val*quotient)
        return ''.join(roman)


if __name__ == '__main__':
    try:
        num = sys.argv[1]
        print(arabic_to_roman(num))
    except IndexError:
        print("Missing 1 required positional argument")
