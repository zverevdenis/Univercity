month = int(input())
day = int(input())
if month == 2:
    if day == 28:
        print(f"1 - {month + 1} - 2022")
    else:
        print(f"{day + 1} - {month} - 2022")
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        print(f"1 - {month + 1} - {month} - 2022")
    else:
        print(f"{day + 1} - {month} - 2022")
else:
    if day == 31:
        if month == 12:
            print(f"1 - 1 - 2023")
        else:
            print(f"1 - {month + 1} - 2022")
    else:
        print(f"{day + 1} - {month} - 2022")