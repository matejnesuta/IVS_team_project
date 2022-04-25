import re
import sys
import cProfile

lines = sys.stdin.readlines()

nums = ""
for i in lines:
    nums+=i

nums = re.sub(r"[ \t\n]+", "+", nums)

profile = cProfile.Profile()
profile.enable()

print(nums)

profile.disable()
profile.print_stats(sort='time')
profile.dump_stats("profiling_calc.prof")
