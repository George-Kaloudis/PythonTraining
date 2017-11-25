'''
Python Mini Project Ασκηση 6.2
'''
import time
jpg=[255,216,255]
isjpg = True
try:
    with open('imag','rb') as f:
        byte = list(f.read(3))
except Exception as err:
    print("Κατι πηγε λάθος στο ανοιγμα του αρχειου. Τυπος λαθους:",type(err))
for index, obj in enumerate(byte):
    print(obj,hex(obj))
    if jpg[index] != obj:
        isjpg = False

if isjpg:
    print("Το αρχείο ειναι τύπου jpg")
else:
    print("Το αρχείο ΔΕΝ ειναι τύπου jpg")

time.sleep(10)
