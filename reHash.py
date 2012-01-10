# reHash - Decrypts SHA-1 and MD5 hashes up to 5 characters long
# (Hashes longer than 5 characters would take enormous amounts of time to solve with this method)
# Created by David Gedarovich
# http://www.github.com/Dave-G
# gedarovich@hotmail.com
# Updated 1/10/12

import os
import hashlib

# Main function
def decrypt(x):
	i = 0
	ii = 0
	iii = 0
	iiii = 0
	iiiii = 0
	c = 0
	# 1 character case
	while (i < len(alpha)):
		c += 1
		os.system('cls')
		print "Decrypting: " + x
		# SHA-1
		if (hashType == 'sha1'):
			print "Trying: " + hashlib.sha1(alpha[i]).hexdigest() + " (" + alpha[i] + ")"
			print "Combinations Tried: " + str(c)
			if (hashlib.sha1(alpha[i]).hexdigest() == x):
				print "Success! Decrypted to: " + alpha[i]
				i = 0
				break
			else:
				i += 1
		# MD5
		elif (hashType == 'md5'):
			print "Trying: " + hashlib.md5(alpha[i]).hexdigest() + " (" + alpha[i] + ")"
			print "Combinations Tried: " + str(c)
			if (hashlib.md5(alpha[i]).hexdigest() == x):
				print "Success! Decrypted to: " + alpha[i]
				i = 0
				break
			else:
				i += 1
	# 2 character case
	if (i == len(alpha)):
		i = 0
		while (ii < len(alpha)):
			c += 1
			os.system('cls')
			print "Decrypting: " + x
			# SHA-1
			if (hashType == 'sha1'):
				print "Trying: " + hashlib.sha1(alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.sha1(alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[ii] + alpha[i]
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
			# MD5
			elif (hashType == 'md5'):
				print "Trying: " + hashlib.md5(alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.md5(alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[ii] + alpha[i]
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
	# 3 character case
	if (ii == len(alpha)):
		i = 0
		ii = 0
		while (iii < len(alpha)):
			c += 1
			os.system('cls')
			print "Decrypting: " + x
			# SHA-1
			if (hashType == 'sha1'):
				print "Trying: " + hashlib.sha1(alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.sha1(alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iii] + alpha[ii] + alpha[i]
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
					if (ii == len(alpha)):
						ii = 0
						iii += 1
			# MD5
			elif (hashType == 'md5'):
				print "Trying: " + hashlib.md5(alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.md5(alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iii] + alpha[ii] + alpha[i]
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
					if (ii == len(alpha)):
						ii = 0
						iii += 1
	# 4 character case
	if (iii == len(alpha)):
		i = 0
		ii = 0
		iii = 0
		while (iii < len(alpha)):
			c += 1
			os.system('cls')
			print "Decrypting: " + x
			# SHA-1
			if (hashType == 'sha1'):
				print "Trying: " + hashlib.sha1(alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.sha1(alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
					if (ii == len(alpha)):
						ii = 0
						iii += 1
					if (iii == len(alpha)):
						iii = 0
						iiii += 1
			# MD5
			elif (hashType == 'md5'):
				print "Trying: " + hashlib.md5(alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.md5(alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
					if (ii == len(alpha)):
						ii = 0
						iii += 1
					if (iii == len(alpha)):
						iii = 0
						iiii += 1
	# 5 character case
	if (iiii == len(alpha)):
		i = 0
		ii = 0
		iii = 0
		iiii = 0
		while (iii < len(alpha)):
			c += 1
			os.system('cls')
			print "Decrypting: " + x
			# SHA-1
			if (hashType == 'sha1'):
				print "Trying: " + hashlib.sha1(alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiiii]+ alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.sha1(alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
					if (ii == len(alpha)):
						ii = 0
						iii += 1
					if (iii == len(alpha)):
						iii = 0
						iiii += 1
			# MD5
			elif (hashType == 'md5'):
				print "Trying: " + hashlib.md5(alpha[iiiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiiii]+ alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.md5(alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
					if (ii == len(alpha)):
						ii = 0
						iii += 1
					if (iii == len(alpha)):
						iii = 0
						iiii += 1

# User Interface and console input
# Get hash type and value from user, exit if invalid
hashType = raw_input("Hash Type?(sha1/md5): ")
if (hashType != 'sha1' and hashType != 'md5'):
	print "Invalid input (not sha1 or md5)"
	os.system('pause')
	exit(1)
input = raw_input("Input hash to decrypt: ")
# SHA-1 must be 40 characters long
if (len(input) != 40 and hashType == 'sha1'):
	print "You did not enter a valid SHA1 hash (40 characters)"
	os.system('pause')
	exit(1)
# MD5 must be 32 characters long
elif (len(input) != 32 and hashType == 'md5'):
	print "You did not enter a valid MD5 hash (32 characters)"
	os.system('pause')
	exit(1)
# Set up the list to use in testing
alpha = list('abcdefghijklmnopqrstuvwxyz')
# Additional tests may be added, but they exponentially increase the time taken
input2 = raw_input("Include upper-case?(y/n): ")
if (input2 == 'y'):
	alpha.extend(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
input3 = raw_input("Include numbers?(y/n): ")
if (input3 == 'y'):
	alpha.extend(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
# Decrypt and show answer
decrypt(input)
os.system('pause')
exit(0)