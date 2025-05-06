day = int(input("Enter week day in number: "))
match day:
#   you can user two input 1 and 11 to check the day is Monday.
#   case 1 | 11:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print('Enter range from 1 - 7 only')

