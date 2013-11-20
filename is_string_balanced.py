#!/usr/bin/env python 

"""
 Your task in this exercise is as follows:

    Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
    Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest. 

Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
"""

import random 

def word_generator(com_str, com_length, max_generator):

    for count in xrange(0,max_generator):
          random_selection = random.sample(com_str, com_length)
	  com_str = "".join(random_selection)
          com_str = com_str.strip()
	  indx = 0 
	  opn_br = 0
	  cls_br = 0
	  rotate = True
	  while rotate == True:
	      
              if com_str[indx] == "[":
	          opn_br += 1

	      if com_str[indx] =="]":
	          cls_br +=1

	      if opn_br < cls_br:
	          rotate = False
		  print com_str, ":Not ok"
		
	      indx +=1	

	      if indx == len(com_str):
	          rotate = False
		  print com_str, ":Ok"
	
	          
	  
if __name__=="__main__":
    
    length =  int(raw_input("enter the length for open and closed bracket :"))
    max_generator = int(raw_input("HOw many combination you want to build: "))
    opn_br = "[" *length
    cls_br = "]" *length
    com_str = opn_br+cls_br
    
    word_generator(com_str, length*2, max_generator)




	    

