#Provides funciton and variable related to the python runtime environment
#import sys module 
import sys

#Check Version
print(sys.version)

#Location of file
print(sys.executable)

#System running file
print(sys.platform)

#stdin ask for input from user
for line in sys.stdin:
    if line.strip() == 'exit':
        break
    #stout outputs user's input
    sys.stdout.write('>> {}'.format(line))

for i in range(1, 5):
    sys.stdout.write(str(i))
    sys.stdout.flush()

for i in range(1 ,5):
    print(i)

#Show status bar
import time 

for i in range(0, 51):
    time.sleep(0.1)
    #\r to start infront of the line when write in {}{}
    sys.stdout.write('{} [{}{}]\r'.format(i, '#' * i, '.'*(50-i) ))
    sys.stdout.flush()
sys.stdout.write('\n')

#Name of the file and add arguments
print(sys.argv)

#If input is no longer then 3 character
if len(sys.argv) !=3:
    print('[X] To run {} enter a username and password '.format(sys.argv[0] ))


username = sys.argv[0]
password = sys.argv[1]

print('{}{}'.format(username, password))

#Search for modules

