word_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

with open("input1.txt") as input_file:
    total = 0
    digits = ["", ""]
    for line in input_file:
        for word in range(0, 10):
            #line = line.replace(word_numbers[word], number_numbers[word])
            line_pos = line.find(word_numbers[word])
            if line_pos != -1:
                line = line[:line_pos] + number_numbers[word] + line[line_pos:]
        print(line)
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