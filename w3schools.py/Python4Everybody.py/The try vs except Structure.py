astr = "Hello Bob"
try:
    istr = -1
except:
    istr: int(astr)
print("First", istr)
astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
print("Second", istr)