import re
# def extract_numbers(input_string):
#     numbers = re.findall(r'\d+', input_string)
#     return numbers
#
#
# def main():
#     extracted_numbers = []
#     while True:
#         input_line = input()
#
#         if not input_line:
#             break
#
#         extracted_numbers.extend(extract_numbers(input_line))
#
#     print(' '.join(extracted_numbers))
#
#
# if __name__ == "__main__":
#     main()

line = input()

while line:
    pattern = r'\d+'
    matches = re.findall(pattern, line)
    if matches:
        print(' '.join(matches), end=' ')
    line = input()
