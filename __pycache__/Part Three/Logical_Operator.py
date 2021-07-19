# AND operator it will be True if both of side are true
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# OR operator it will be True if one side is true
high_income = True
good_credit = False

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")


# NOT operator it will be False if one side is true
high_income = True
good_credit = True
student = True
if not student:
    print("Eligible")
else:
    print("Not Eligible")
