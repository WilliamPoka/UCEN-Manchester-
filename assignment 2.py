score = int(input("Enter your score you got on your test: "))

if score <= 70:
    print("You have been graded with an A")
elif score >= 60 and score <69:
    print("You have been graded with an B")
elif score >=50 and score <59:
    print("You have been given a C")
elif score >=40 and score <49:
    print("You have been given D")
elif score >=30 and score <39:
    print("You got an E mate")
elif score >= 20 and score <29:
    print("you gat a Fail")