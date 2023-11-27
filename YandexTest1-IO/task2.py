split_char = ' '
INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'

with open(INPUT_FILE, encoding="utf8", mode='r') as file:
    (a, b) = [int(x) for x in file.readline().split(split_char)]

res = a + b
with open(OUTPUT_FILE, encoding='utf8', mode='w') as file:
    file.write(str(res))