Below deck troubles: Cat code
====================================

## Task
Ahoy, officer,

due to the lack of developers on board, the development of the access code generator for the satellite connection was entrusted to the cat of the chief officer. Your task is to analyze the cat's creation and find out the code.

May you have fair winds and following seas!

Download the cat code.
(MD5 checksum: aac150b3f24e5b047ee99e25ad263f56)

## Solution
In downloaded archive are 2 files: meow.py and meowmeow.py. Let's run meowmeow.py:

	python3 meowmeow.py 
	Who rules the world? me
	Who rules the world?

Ok, so look inside file :-) Right answer probably be kittens. And now the script is running... and will be probably for long time. So, look in meow.py. There is a one recursion function:

	def meow(kittens_of_the_world):
	    """
	    meowwwwww meow
	    """
	    print('meowwww ', end='')
	    if kittens_of_the_world < UNITED:
	        return kittens_of_the_world
	    return meow(kittens_of_the_world - UNITE) + meow(kittens_of_the_world - UNITED)

First, I commented print line so stdout stays clear. Second, very probably there will be some more effective solution than recursive function. But in late hours, my tired mind came with ugly fast solution: recursive function is called very often with same argument and it only ends when it reaches under 2. So, add cache:

	CACHE = {}

	def meow(kittens_of_the_world):
	    """
	    meowwwwww meow
	    """
	    #print('meowwww ', end='')
	    if kittens_of_the_world in CACHE:
	        return CACHE[kittens_of_the_world]
	    if kittens_of_the_world < UNITED:
	        return kittens_of_the_world
	    result = meow(kittens_of_the_world - UNITE) + meow(kittens_of_the_world - UNITED)
	    CACHE[kittens_of_the_world] = result
	    return result

And run program again:

	python3 meowmeow.py 
	Who rules the world? kittens
	meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww meowwww 
	FLAG{YcbS-IAbQ-KHRE-BTNR}

Fixed program is in repository.