# 8*6
import numpy as np
import time
import math

def tobase64(number):
	base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
	n = math.ceil(highestbit(number)/6.0)
	b64 = ""
	for i in range(n):
		b64 += base64[(number&63)] 
		number = number >> 6
	return b64

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

def highestbit(number):
	number = int(number)
	n = 0
	while(number!=0):
		number = number >> 1
		n = n + 1
	return n

start = time.time()



# data structure of each skill tree:
# id: 			0 1 2 3 4 5 6 7 8 9
# max points:	4 2 2 3 2 4 2 4 4 3
# current pts:  0 0 0 1 0 0 0 0 1 1

N = 21

sk_tree = np.zeros((N,3))

#id de cada skill
for i in range(N):
	sk_tree[i,0] = i
#maximo de skills
sk_tree[:,1] = np.array([3,1,1,2,1,3,1,3,3,2,3,1,1,3,1,1,3,2,2,1,1])
#10*1 +11*2
#skill atuais
#sk_tree[:,2] = np.array([0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0])
sk_tree[:,2] = np.array([3,1,1,2,1,3,1,3,1,2,3,0,1,2,0,0,2,1,2,1,0])
#sk_tree[:,2] = sk_tree[:,1]
#print(sk_tree)

#se   0<= max < 2, só preciso de um bit
#se   1 < max < 4, preciso de 2 bits
#se max >= 4, preciso de 3 bits

#hash
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

print("Hash convertido em alfanumerico: ",tobase64(hsh))

print("Hash obtido do alfanumerico: " ,frombase64(tobase64(hsh)))

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

print("Tempo passado:",-start + time.time())

#print(highestbit(2))

#tobase64()


"""
print(len(teste))
tm = teste.upper()
tm = '0123456789'+tm+teste
print(len(tm))
print(tm)

print(ord('z'))
print(chr(60))
"""


#3453q94tmhov3w94ty34txe5v84ybn93w8