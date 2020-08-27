# 8*6
import numpy as np
import time
import math

#the traditional base64 is defined by:
#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
#however, due to url encoding, we shall change '+','/' to '-','_'
#letting us with our base 64 as:
#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_


#convert a number to base64
#base 64 ocupies 55.36% of the space of a number represented in base 10
#as log_{64} 10 = 0.5536
#e.g.: 
#a 10 digit number in base 10 is a 6(5.536 rounded up) digit number in base64
#and 1 character in base64 equals 6 characters in base 2, as 2^6=64.
def tobase64(number):
	base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
	n = math.ceil(highestbit(number)/6.0)#get the number of characters needed
	b64 = ""
	for i in range(n):
		b64 += base64[(number&63)]#get the least 6 significant bits
		number = number >> 6 #shifts the number right in 6 bits
	return b64

#convert a string in this base 64 to number 
def frombase64(string):
	valor = 0
	for ind,caracter in enumerate(string):
		a = ord(caracter)
		aux = 0
		if(ord('Z') >= a >= ord('A')):
			aux = a-ord('A')
		elif(ord('z') >= a >= ord('a')):
			aux = a-ord('a')+26
		elif(ord('9') >= a >= ord('0')):
			aux = a-ord('0')+52
		elif(caracter == '-'):
			aux = 62
		elif(caracter == '_'):
			aux = 63
		aux = aux << (6*ind)
		valor = valor | aux
	return valor

#get the position(first) of the highest value bit in a number
#eg: 5 -> 1 0 1   #eg: 23 -> 1 0 1 1 1    #eg: 1 -> 0 1   #eg: 0 -> 0 0 
#         3 2 1   #          5 4 3 2 1    #         2 1   #         2 1    
# returns 3       #  returns 5            # returns 1     # returns 0
#		  	
def highestbit(number):
	number = int(number)
	n = 0
	while(number!=0):
		number = number >> 1
		n = n + 1
	return n


#measuring the time spent on the code
start = time.time()


# data structure of each skill tree:
# id: 			sk_tree[:,0]
# max points:	sk_tree[:,1]
# current pts:  sk_tree[:,2]
N = 21
sk_tree = np.zeros((N,3))

#id of each skill
for i in range(N):
	sk_tree[i,0] = i

#maximum of skill point in each node of the skill tree
sk_tree[:,1] = np.array([3,1,1,2,1,3,1,3,3,2,3,1,1,3,1,1,3,2,2,1,1])
#max 1 is represented in 1 bit, max 2 or 3 are represented by 2 bits
#max 4,5,6,7 are represented by 3 bits...
#therefore, this skill tree ocuppies 10*1 + 11*2 = 32 bits at max

#actual count of skill points in each node
sk_tree[:,2] = np.array([0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0])
#sk_tree[:,2] = np.array([0,1,1,2,1,3,1,3,1,2,3,0,1,1,0,0,2,1,2,1,1])
#sk_tree[:,2] = sk_tree[:,1]
#print(sk_tree)


#max 1 is represented in 1 bit, max 2 or 3 are represented by 2 bits
# bits:  		... 0	0	0	0	0	0	0	0	0	0	0	0	0	0
# bit offset:	... 13	12	11	10	9	8	7	6	5	4	3	2	1	0
#					 \ /	 \	/	|	 \ /	|	 \ /	|	|	 \ /
# skill:			  8		  7		6	  5		4	  3		2	1	  0
# max of skill:		  3		  3		1	  3		1	  2		1	1	  3	

#hashing:
hsh = 0
tam = 0
place = 0
for i in range(N):
	a = int(sk_tree[i,1])#valor max
	b = int(sk_tree[i,2])#valor atual
	b = min(a,b)#checa se o valor atual é menor que o máximo
	b = b << tam
	hsh = hsh | b
	tam += highestbit(a)

print("Hash:", hsh)

print("Hash converted to alfanumerico: ",tobase64(hsh))

print("Hash gotten from alfanumerico: " ,frombase64(tobase64(hsh)))

hash_novo = frombase64(tobase64(hsh))
vetor = np.zeros((N))
for i in range(N):
	a = int(sk_tree[i,1])#valor max
	hbit = highestbit(a)
	b = ((1<<hbit)-1) & hash_novo
	vetor[i] = min(a,b) 
	hash_novo = hash_novo >> hbit

print("Vetor de skills original:")
print(sk_tree[:,2])
print("Vetor de skills gerado pelo hash:")
print(vetor)

#print(vetor-sk_tree[:,2])

#measuring the time spent on the code
print("Time elapsed:",-start + time.time())

