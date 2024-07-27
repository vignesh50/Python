def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
        return 1
      else:
        print("Not leap year")
    else:
      print("Leap year")
      return 1
  else:
    print("Not leap year")

leap = is_leap(2023)

print(leap)
  

