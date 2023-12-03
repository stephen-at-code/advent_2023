with open("input1.txt") as input_file:
    total = 0
    digits = ["", ""]
    for line in input_file:
        for char in line:
            if char.isdigit():
                if digits[0] == "":
                    digits[0] = char
                    digits[1] = char
                else:
                    digits[1] = char
        total = total + int(digits[0] + digits[1])
        digits = ["", ""]
print(total)
    