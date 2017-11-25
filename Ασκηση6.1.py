'''
Python Mini Project Ασκηση 6.1
'''
import time

try:
    with open('cities.txt','r') as f:
        lines = f.readlines()
except Exception as err:
    print("Κατι πηγε λάθος στο ανοιγμα του αρχειου. Τυπος λαθους:",type(err))


for index, line in enumerate(lines):
    lines[index]=str(index+1)+": "+line

try:
    with open('out.txt','w') as f:
        for line in lines:
            f.write(line)
except Exception as err:
    print("Κατι πηγε λάθος στο ανοιγμα του αρχειου. Τυπος λαθους:",type(err))

time.sleep(10)
