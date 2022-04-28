import re
import sys
import cProfile
from mathlib.calc_exp import calc_output, is_neg_oprnd, to_neg_oprnd


lines = sys.stdin.readlines()

nums = ""
for i in lines:
    nums+=i

nums = nums.strip()
nums = re.sub(r"([ \t\n\r])+", "+", nums)

minus = (nums.split("+"))
nums = ""
for i in minus:
    print(i)
    if not (re.match(r"([-]?\d+)",i)):
        raise SystemExit('spatne zadany vstup')
    
    if (i[0]=='-'):
        nums+=to_neg_oprnd(i)+"+"
    else:
        nums+=i+"+"    

nums=nums[:-1]

exps = (nums.split("+"))
expNums = ""
for i in exps:
    i+="^2"
    expNums+=i+"+"

expNums=expNums[:-1]

count = str(nums.count("+")+1)

profile = cProfile.Profile()
profile.enable()

sum = str(calc_output(nums))
if (sum[0]=='-'):
        sum=to_neg_oprnd(sum)

avg = str(calc_output(sum+"/"+count))
if (avg[0]=='-'):
        avg=to_neg_oprnd(avg)

powSum = str(calc_output(expNums))
b = str(calc_output(count+"*"+avg+"^2"))
c = str(calc_output(powSum+"-"+b))
if (c[0]=='-'):
        c=to_neg_oprnd(c)

sum2 = str(calc_output(sum+"-1"))

if (sum2[0]=='-'):
        sum2=to_neg_oprnd(sum2)

d = str(calc_output(c+"/"+sum2))

if (d[0]=='-'):
        d=to_neg_oprnd(d)

#TODO: FLIP CISEL TADY
result = str(calc_output("nrt(2,"+d+")"))

print(result)
# print(nums)

profile.disable()
profile.print_stats(sort='time')
profile.dump_stats("profiling_calc.prof")
