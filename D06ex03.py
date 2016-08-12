def main():
    """ write ten random numbers to a file
    """

f = open('roster.txt', 'r')

list1 = list()

while True:
	line1 = f.readline()
	if line1 == '':
		break
	name = line1.split()[0]
	if name.find('e') != -1:
		list1.append(name)


for item in list1:
	print(item)
print(len(list1))

if __name__ == '__main__':
    main()
