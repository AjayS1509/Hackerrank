# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input();

for i in range(int(n)):
    key = input();
    try:
        re.compile(key)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid);
