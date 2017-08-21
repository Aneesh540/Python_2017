""" READING FROM EXISTING FILE """

f = open('test.txt','r')
print(f.name)					# give name of file
print(f.mode)					# gives mode of file
print(f.tell())					# tells current position of file
f.close()						

def function():
	with open('test.txt','r') as f:
		f_contents = f.read()					# gives full content as a single string
		print(f_contents)


	with open("test.txt", 'r') as f3:
		f3_contents = f3.readline()				# in readline() cursor goes to next line after execution
		print(f3_contents)						# but once with statement is closed it'll start again

		f3_contents = f3.readline()
		print(f3_contents)	



def memory_efficient(path,mode):
	""" this for loop will iterate through one at a time """

	with open(path,mode) as f:

		for line in f:
			print(line)


def reading_chunks():
	
	f = open('test.txt','r')
	print(f.read(15))			# reads only 15 character
	print('*'*25)
	print(f.read(15))			# then starting from next 15
	
	print('presently curser is @:',f.tell())

	f.seek(0)					# reset to starting position if seek(5) then start @ 5th character

	print(" now I'am @ position %s" % f.tell())
	f.close()


reading_chunks()	
memory_efficient('test.txt','r')
