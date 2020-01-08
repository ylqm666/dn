import sys

alice_status = True

def alice_false():
  print("Alice")
  global alice_status
  alice_status = False

def main(lines):
  global alice_status
  red_flag = False
  white_flag = False
  input_list = lines[0].split()
  for i in input_list:
    if i == "RU":
      if red_flag is False:
        red_flag = True
      else:
        alice_false()
        break
    elif i == "RD":
      if red_flag is True:
        red_flag = False
      else:
        alice_false()
        break
    elif i == "WU":
      if white_flag is False:
        white_flag = True
      else:
        alice_false()
        break
    elif i == "WD":
      if white_flag is True:
        white_flag = False
      else:
        alice_false()
        break
  if alice_status == True:
    print("Simon")
    ans = ""
    if red_flag is True:
      ans += "U"
    else:
      ans += "D"
    if white_flag is True:
      ans += "U"
    else:
      ans += "D"
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
