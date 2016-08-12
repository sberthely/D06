def main():
    """ write ten random numbers to a file
    """
import random
f = open('D06ex02.txt', 'w')
for i in range(0,10):
	f.write(str(random.randint(1, 1000)) +  '\n')

if __name__ == '__main__':
    main() 