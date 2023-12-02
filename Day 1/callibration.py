import re

digit_dict = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

text_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# def parse_text(text):
#     final_str = ""
#     text_str = ""
#     for char in text:
#         if 
#     for key in digit_dict:
#        if key in text: 
#            text = text.replace(key, digit_dict[key])
#            break
       
#     "".join(char for char in text if char.isalpha())
    
#     return text

def find_callibration_values(text: str):
    call_value = ""
    text_value = ""
    for char in text:
        if char.isdigit():
            call_value += char
            break
        else:
            text_value += char
            for digit in digit_dict:
                if re.search(digit, text_value):
                    call_value += digit_dict[digit]
                    break
            else:
                continue
            break
                
    text_value = ""
    for char in text[::-1]:
        if char.isdigit():
            call_value += char
            break
        else: 
            text_value += char
            for digit in digit_dict:
                if re.search(digit, text_value[::-1]):
                    call_value += digit_dict[digit]
                    break
            else: 
                continue
            break

    return int(call_value)


def final_sum(values):
    sum = 0
    for value in values:
        sum += value
    return sum

def main():
    callibration_codes = []
    with open("input.txt", 'r') as file:
        for line in file:
            callibration_codes.append(find_callibration_values(line))

    print(f"The final sum of all the callibration values in the input is: ", final_sum(callibration_codes))
    

if __name__ == "__main__":
    main()