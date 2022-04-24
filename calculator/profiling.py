import re
import sys

lines = sys.stdin.readlines()

nums = ""
for i in lines:
    nums+=i

nums = re.sub(r"[ \t\n]+", "+", nums)
print(nums)
