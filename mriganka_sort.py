# mriganka_sort(arg), is a function made by my own sorting Algorithm. Feel free to use it. It take one argument(arg) as a list and return a sorted list. @

def mriganka_sort(b):
	c = len(b)
	e = 0
	d = True
	while int(d) == 1:
			for i in range(c - 1):
				if b[i] > b[i + 1]:
					b[i], b[i + 1] = b[i + 1], b[i]
					e += 1
			if e == 0:
					d = False
			e = 0
	return b
	
c = [3, 4, 2, 9, 7]
print(mriganka_sort(c))
