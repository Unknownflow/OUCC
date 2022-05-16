date_input = input()

def valid(date_input):
  year = date_input[0:4]
  month = date_input[5:7]
  date = date_input[8:]
  if len(date_input) == 10:
    if date_input[4] == '-' and date_input[7] == '-' and year.isdigit() and month.isdigit() and date.isdigit():
      if 1900 <= int(year) <= 2020 and 0 < int(month) <= 12 and 0 < int(date) <= 31:
        return True
  
  return False
  
print(valid(date_input))
