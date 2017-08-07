#! /usr/bin/env python3
import sys
import re
# from math import sqrt

def test(a1, a2):
        """
                This section is a comment
                This function print some stuff
        """
        print(a1, a2)

def resolve_simple(arg):
	equa = arg.split('=')
	equa = equa[0].split(' ')
	a = equa[0].replace('x', '')
	if a == '':
		a = '1'
	if a == '-':
		a = '-1'
	a = float(a)
	b = equa[2]
	b = float(b)
	b = b * -1 if equa[1] == '-' else b
	result = b * -1 / a
	print(float(result))

def descriminant(a, b, c):
	des = b * b - 4 * a * c
	return des

def calculate_simple(b, c):
	x = -c / b
	print("The solution is:\n" + str(x))

def calculate_premier(des, a, b, c):
	x = -b / (2*a)
	print('Discriminant is null, the solution is:')
	print(x)

def calculate_second(a, b, c):
	des = descriminant(a, b, c)
	if des < 0:
		print('No solution\n')
		return
	if des == 0:
		calculate_premier(des, a, b, c)
		return
	print('Discriminant is strictly positive, the two solutions are:')
	x1 = (-b + des**0.5) / (2*a)
	x2 = (-b - des**0.5) / (2*a)
	print(x1)
	print(x2)




# V2
def x_detail(tab):
	c = 1.0
	first = 0
	l = len(tab)
	i = 0
	while i < l:
		try:
			if first == 0:
				c *= float(tab[i])
				first = 1
			else:
				if tab[i - 1] == '*':
					c *= float(tab[i])
				elif tab[i - 1] == '/':
					c /= float(tab[i])
		except:
			pass
		i += 1
	return c

def decompose_x_detail_v2(d, s):
	v = re.search('X\^-?[0-9]*.?[0-9]', s)
	if v:
		v = v.group(0)
		if v in d:
			d[v] += x_detail(s.split(' '))
		else:
			d[v] = x_detail(s.split(' '))
	# else:
	# 	d['c'] += x_detail(s.split(' '))
	return d

def decompose_x(s):
	d = {}
	tab = s.split('+')
	for v in tab:
		d = decompose_x_detail_v2(d, v)
	return d


def merge_d_v2(left_x, right_x):
	for t in right_x:
		if t not in left_x:
			left_x[t] = 0.0


	for v in left_x:
		if v in right_x:
			left_x[v] -= right_x[v]
	return left_x

def print_reduced_v2_v2(d):
	s = None
	first = 0
	for v in d:
		if d[v] or d[v] == 0.0:
			if s:
				first = 1
				if d[v] >= 0:
					s += ' + '
				else:
					s += ' '
			else:
				first = 0
				s = ''
			i = float(int(d[v]))
			tmp = d[v]
			if i == d[v]:
				tmp = int(d[v])
			tmp = str(tmp)
			if first > 0:
				tmp = tmp.replace('-', '- ')
			s += tmp
			if v != 'c':
				s += ' * ' + v
	print('Reduced form: ' + s + ' = 0')

def check_degre_double(d):
	degre = 0
	degre_f = 0
	for v in d:
		if v == 'c':
			continue
		s = v.replace('X^', '')
		f = float(s)
		i = float(int(f))
		if i != f:
			print("The polynomial degree is double, I can't solve.")
			sys.exit()
		if i < 0:
			print("The polynomial degree is negative, I can't solve.")
			sys.exit()

def print_reduced_degre_v2(d):
	degre = 0
	degre_f = 0
	for v in d:
		if v == 'c':
			continue
		s = v.replace('X^', '')
		f = float(s)
		if f > degre_f:
			degre_f = f

	degre = float(int(degre_f))
	rest = degre_f - degre
	if degre == degre_f:
		degre_f = int(degre_f)
	print('Polynomial degree: '+str(degre_f))
	if degre_f > 2:
		print("The polynomial degree is stricly greater than 2, I can't solve.")
		sys.exit()
	check_degre_double(d)
	return degre_f

def resolve_v2(d, degre):
	tmp = 0
	for v in d:
		if float(d[v]) != 0.0:
			tmp = 1
	if tmp == 0:
		print('Every real are solution.')
		sys.exit()
	if  degre > 1:
		calculate_second(d['X^2'], d['X^1'], d['X^0'])
	else:
		calculate_simple(d['X^1'], d['X^0'])


def v2(s):
	s = s.replace('- ', ' + -')
	s = s.replace('-X', '-1 * X')
	split = s.split('=')
	left = split[0].strip()
	right = split[1].strip()
	left_x = decompose_x(left)
	right_x = decompose_x(right)

	print(left_x)
	print(right_x)

	reduced = merge_d_v2(left_x, right_x)
	print('\n')
	print(reduced)
	print('\n')

	print_reduced_v2_v2(reduced)



	resolve_v2(reduced, print_reduced_degre_v2(reduced))



if __name__ == '__main__':
		# resolve_simple(sys.argv[1])
		v2(sys.argv[1].strip())
		sys.exit()
		if is_infinite_solution(sys.argv[1]) == 1:
			print('Every real number are solution')
			sys.exit()
		# decompose(sys.argv[1])
		tab = sys.argv[1].strip().split('=')
		right = tab[0].strip()
		left = tab[1].strip()
		di_left = decompose_left(left)
		tab_right = decompose_right(right)
		tab_reduced = found_reduced_form(tab_right, di_left)
		print_reduced(tab_reduced)
		print_reduced_degre(tab_reduced)
		tab_reduced = replace_puissance(tab_reduced)
		tab_reduced = sort_puissance(tab_reduced)
		tab_reduced = cast_to_float(tab_reduced)
		tab_reduced = replace_less(tab_reduced)
		tab_reduced = resolve_multi(tab_reduced)
		tab_reduced = resolve_div(tab_reduced)
		resolve(tab_reduced)
		sys.exit()



		a = float(sys.argv[1])
		b = float(sys.argv[2])
		c = float(sys.argv[3])
		des = descriminant(a, b, c)
		if des > 0 :
			calculate_second(des, a, b, c)
		if des < 0:
			print('No solution\n')
		if des == 0:
			print('1 degre bitch\n')
			calculate_premier(des, a, b, c)
