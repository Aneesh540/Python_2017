"""
1) If file does not exist then it will create a new file
if file exist then it will fully overrite this file 

2) copying a full file 

3) reading/copying a binary(.jpg) type file"""

with open('test2.txt','w') as f:
	f.write('1)High_Rated_gabru')
	f.write('2)Blank space')
	f.seek(20)				# start from 20th character

def make_copy(original_name,copy_name):
	""" Creates a copy of original file """
	with open(original_name) as rf:
		with open(copy_name,'w') as wf:

			for line in rf:
				wf.write(line)

make_copy('test2.txt','copy_of_test2.txt')


def copy_binary()				
