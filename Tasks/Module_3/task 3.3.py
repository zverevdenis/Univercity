a = input()
if a.find("f") != -1 and a.rfind("f") != a.find("f"):
    print(a.find("f"), a.rfind("f"))
else:
    print(a.find("f"))