arr = [50, 55, 70, 77, 90, 10, 51]
arrfirst = arr[4:6]
plus = "+"

def myfunc(phoneNumber):
    if len(arr) < 13 and len(arr) > 0:
        print("true")
    else:
        print("not true")

    if phoneNumber in arrfirst:
        print("true")
    else:
        print("not true")

    if plus == "+":
        print("true")
    else:
        print("not true")

myfunc(994505555555)
