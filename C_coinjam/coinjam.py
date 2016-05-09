import sys
from math import sqrt; from itertools import count, islice

from multiprocessing import Pool


def coinjam(N, J):
	temp_jc = "11"
	jamcoins = []
	nontriv_divisors = []
	answer = ""

	if int(N) == len(temp_jc) and verify_jc(temp_jc):
		jamcoins.append(temp_jc)

	counter = 2**(int(J)-1) + 1 # at least J then, 


	while int(J) != len(jamcoins):
		temp_jc = str(bin(counter)[2:])

		if (int(N) == len(temp_jc)):
			nontriv_divisors = verify_jc(temp_jc)

			if (len(nontriv_divisors) == 9):
				jamcoins.append(temp_jc)

				answer += temp_jc + " "
				for div in nontriv_divisors:
					answer += str(div) + " "
				answer += "\n"
		counter+=1

	return answer

def verify_jc(jc):	
	bases = [2,3,4,5,6,7,8,9,10]
	in_bases = []
	if jc[0] == jc[-1] == "1":
		# every digit is either 0 or 1
		for digit in jc:
			if digit != "1" and digit != "0":
				return []
		
		#check if all bases 
		for base in bases:
			number = int(jc,base) # convert the number from given base to decimal
			divisors = find_divisors(number) # find all nontrivial divisors

			if divisors != []: #not prime number
				# find non trivial divisor and append to the list.
				in_bases.append(divisors[0])
	
	#else empty list
	return in_bases


def find_divisors(n):
	# look for divisors, returns [] when number is prime.
	divisors = []
	if n > 1:
		for i in islice(count(2), int(sqrt(n)-1)):
			if n%i != 1:
				divisors.append(i)
	return divisors



if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename = sys.argv[1]

	filename = "C-small-attempt0.in"


	answer = ""
	with open(filename, "r") as f:
		maxcase = f.readline()
		case = 1
		while case < int(maxcase)+1:
			i = f.readline().split()
			op = coinjam(i[0], i[1])
			answer += "Case #" + str(case) + ": \n" + str(op)
			case+=1
	
	with open("C-small-attempt0.out","w") as f:
		f.write(answer)