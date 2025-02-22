import sys
print(sys.argv)
if int(sys.argv[1])%2 ==0 :
    print(f"{sys.argv[1]} is even")
else:
    print(f"{sys.argv[1]} is odd")