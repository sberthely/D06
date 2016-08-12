def main():
    """ write ten random numbers to a file
    """

f = open('roster.txt', 'r')

list1 = list()

while True:
	line1 = f.readline()
	if line1.find('e') != -1:
		list1.append(line1)
	if line1 == '':
		break

w = open('D06ex04.txt', 'w')
for item in list1:
	w.write(item)
w.write(str(len(list1)))

if __name__ == '__main__':
    main() 