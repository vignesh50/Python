
check_another = True
while check_another:
    cost = int(input("Enter Amount: "))
    validity = int(input("Enter Validity Days: "))
    cost_per_day = cost / validity

    print(f"Cost Per Day Rs: {cost_per_day:.3f}")

    check_another = int(input("Do you want to continue: Yes:1 or No:0 -> "))