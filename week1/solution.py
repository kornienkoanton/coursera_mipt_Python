import sys
digit_string = sys.argv[1]
#summary = 0
#for digit in digit_string:
#   summary += int(digit)
#print (summary)
print(sum([int(x) for x in sys.argv[1]]))