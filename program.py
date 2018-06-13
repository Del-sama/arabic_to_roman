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
        if num < 1:
            raise ValueError("Number doesn't exist")

        if num in arab_to_rom.keys():
            return(arab_to_rom[num])

        for key, val in arab_to_rom.items():
            a, num = divmod(num, key)
            roman.append(val*a)
        return ''.join(roman)

    except ValueError as e:
        return(e)
