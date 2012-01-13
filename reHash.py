# reHash - Decrypts SHA-1 and MD5 hashes up to 6 characters long
# (Hashes longer than 6 characters would take enormous amounts of time to solve with this method)
# Created by David Gedarovich
# http://www.github.com/Dave-G
# gedarovich@hotmail.com
# Updated 1/13/12

# Imported libraries
import os
import hashlib
import time
import math
import sys

# Main function
def decrypt(x, y):
	# Variables corresponding to string indices, counter, starting point, completion, and starting time
	i = 0
	ii = 0
	iii = 0
	iiii = 0
	iiiii = 0
	iiiiii = 0
	c = 0
	startPoint = 0
	complete = 0
	startTime = time.time()
	# Set starting string (if given)
	if (len(y) > 0):
		# Ignore starting string if it is too long
		if (len(y) > 6):
			print "String too long, ignoring."
			os.system('pause')
		# Make sure every character of the string is in the list
		elif (len(y) == 6 and y[0] in alpha and y[1] in alpha and y[2] in alpha and y[3] in alpha and y[4] in alpha and y[5] in alpha):
			i = alpha.index(y[5])
			ii = alpha.index(y[4])
			iii = alpha.index(y[3])
			iiii = alpha.index(y[2])
			iiiii = alpha.index(y[1])
			iiiiii = alpha.index(y[0])
			startPoint = 5
		elif (len(y) == 5 and y[0] in alpha and y[1] in alpha and y[2] in alpha and y[3] in alpha and y[4] in alpha):
			i = alpha.index(y[4])
			ii = alpha.index(y[3])
			iii = alpha.index(y[2])
			iiii = alpha.index(y[1])
			iiiii = alpha.index(y[0])
			startPoint = 4
		elif (len(y) == 4 and y[0] in alpha and y[1] in alpha and y[2] in alpha and y[3] in alpha):
			i = alpha.index(y[3])
			ii = alpha.index(y[2])
			iii = alpha.index(y[1])
			iiii = alpha.index(y[0])
			startPoint = 3
		elif (len(y) == 3 and y[0] in alpha and y[1] in alpha and y[2] in alpha):
			i = alpha.index(y[2])
			ii = alpha.index(y[1])
			iii = alpha.index(y[0])
			startPoint = 2
		elif (len(y) == 2 and y[0] in alpha and y[1] in alpha):
			i = alpha.index(y[1])
			ii = alpha.index(y[0])
			startPoint = 1
		elif (len(y) == 1 and y[0] in alpha):
			i = alpha.index(y[0])
		# Ignore starting string if it is not in the list
		else:
			print "String not in list, ignoring."
			os.system('pause')
	# First check null string
	if (hashType == 'sha1'):
		if (hashlib.sha1('').hexdigest() == x):
			os.system('cls')
			print "Trying: " + hashlib.sha1('').hexdigest() + " ()"
			print "Combinations Tried: 1"
			print "Success! Decrypted to: <null string> ()"
			if (((time.time() - startTime) % 60) < 1):
				print "Time Taken: Less then 1 second"
			else:
				print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
			complete = 1
			# To skip the next check
			startPoint = 99
	if (hashType == 'md5'):
		if (hashlib.md5('').hexdigest() == x):
			os.system('cls')
			print "Trying: " + hashlib.md5('').hexdigest() + " ()"
			print "Combinations Tried: 1"
			print "Success! Decrypted to: <null string> ()"
			if (((time.time() - startTime) % 60) < 1):
				print "Time Taken: Less then 1 second"
			else:
				print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
			complete = 1
			# To skip the next check
			startPoint = 99
	if (startPoint == 0 and i == 0):
		c += 1
	# 1 character case (first check null string)
	if (startPoint == 0):
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
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
					break
				else:
					i += 1
			# MD5
			elif (hashType == 'md5'):
				print "Trying: " + hashlib.md5(alpha[i]).hexdigest() + " (" + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.md5(alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[i]
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
					break
				else:
					i += 1
		if (complete == 0):
			startPoint = 1
			i = 0
	# 2 character case
	if (startPoint == 1):
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
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
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
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
		if (complete == 0):
			i = 0
			ii = 0
			startPoint = 2
	# 3 character case
	if (startPoint == 2):
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
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
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
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
					break
				else:
					i += 1
					if (i == len(alpha)):
						i = 0
						ii += 1
					if (ii == len(alpha)):
						ii = 0
						iii += 1
		if (complete == 0):
			i = 0
			ii = 0
			iii = 0
			startPoint = 3
	# 4 character case
	if (startPoint == 3):
		while (iiii < len(alpha)):
			c += 1
			os.system('cls')
			print "Decrypting: " + x
			# SHA-1
			if (hashType == 'sha1'):
				print "Trying: " + hashlib.sha1(alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.sha1(alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
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
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
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
		if (complete == 0):
			i = 0
			ii = 0
			iii = 0
			iiii = 0
			startPoint = 4
	# 5 character case
	if (startPoint == 4):
		while (iiiii < len(alpha)):
			c += 1
			os.system('cls')
			print "Decrypting: " + x
			# SHA-1
			if (hashType == 'sha1'):
				print "Trying: " + hashlib.sha1(alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.sha1(alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
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
					if (iiii == len(alpha)):
						iiii = 0
						iiiii += 1
			# MD5
			elif (hashType == 'md5'):
				print "Trying: " + hashlib.md5(alpha[iiiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.md5(alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
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
					if (iiii == len(alpha)):
						iiii = 0
						iiiii += 1
		if (complete == 0):
			i = 0
			ii = 0
			iii = 0
			iiii = 0
			iiiii = 0
			startPoint = 5
	# 6 character case
	if (startPoint == 5):
		while (iiiiii < len(alpha)):
			c += 1
			os.system('cls')
			print "Decrypting: " + x
			# SHA-1
			if (hashType == 'sha1'):
				print "Trying: " + hashlib.sha1(alpha[iiiiii] + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiiiii] + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.sha1(alpha[iiiiii] + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiiiii] + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
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
					if (iiii == len(alpha)):
						iiii = 0
						iiiii += 1
					if (iiiii == len(alpha)):
						iiiii = 0
						iiiiii += 1
			# MD5
			elif (hashType == 'md5'):
				print "Trying: " + hashlib.md5(alpha[iiiiii] + alpha[iiiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() + " (" + alpha[iiiiii] + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i] + ")"
				print "Combinations Tried: " + str(c)
				if (hashlib.md5(alpha[iiiiii] + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]).hexdigest() == x):
					print "Success! Decrypted to: " + alpha[iiiiii] + alpha[iiiii] + alpha[iiii] + alpha[iii] + alpha[ii] + alpha[i]
					if (((time.time() - startTime) % 60) < 1):
						print "Time Taken: Less then 1 second"
					else:
						print "Time Taken: " + str(int(math.floor(((time.time() - startTime) / 60) / 60))) + " hours " + str(int((math.floor((time.time() - startTime) / 60)) % 60)) + " minutes " + str(int((time.time() - startTime) % 60)) + " seconds"
					complete = 1
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
					if (iiii == len(alpha)):
						iiii = 0
						iiiii += 1
					if (iiiii == len(alpha)):
						iiiii = 0
						iiiiii += 1

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
	print "You did not enter a valid SHA-1 hash (40 characters)"
	os.system('pause')
	exit(1)
# MD5 must be 32 characters long
elif (len(input) != 32 and hashType == 'md5'):
	print "You did not enter a valid MD5 hash (32 characters)"
	os.system('pause')
	exit(1)
# Set up the list to use in testing
alpha = list('abcdefghijklmnopqrstuvwxyz')
# Additional tests may be added, but they greatly increase the time taken
input2 = raw_input("Include upper-case?(y/n): ")
if (input2 == 'y'):
	alpha.extend(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
input3 = raw_input("Include numbers?(y/n): ")
if (input3 == 'y'):
	alpha.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
# Allow user to start from a specified string to promote parallel computing or save time
input4 = raw_input("Begin from a specific string?(leave blank to start from scratch): ")
# Decrypt and show answer with error handling
try:
	decrypt(input, input4)
except:
	os.system('cls')
	print "Fatal Error!" 
	# Show error type and description
	print str(sys.exc_type) + ":" + str(sys.exc_value)
os.system('pause')
# Protect against accidental keypresses leading to loss of data
print "Are you sure you want to exit?"
os.system('pause')
exit(0)