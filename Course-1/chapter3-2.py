score = input("Enter Score: ")
s = float(score)

if s<0:
    print("invalid score")
elif s<0.6:
    print('F')
elif s<0.7:
    print('D')
elif s<0.8:
    print('C')
elif s<0.9:
    print('B')
elif s<1.0:
    print('A')
else:
    print("invalid score")
