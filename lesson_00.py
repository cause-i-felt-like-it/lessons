### LESSON_0: WELCOME TO THE CODE ###

# this is a comment; it starts with a #: it is not code that runs. In pyCharm, press CTRL + /  to uncomment or re-comment a line.
# Uncomment the lines you want, and then run them. If you remove # on a comment, you will end up with nonsense code that will cause
# errors. If 'error' sounds scary, don't worry: errors are more common than code that runs; they just need to be fixed.

# '=' allows us to assign something to a variable
# variable = "<-- this is a variable" # Variables are like boxes that store things.
# print(variable)

### DATA TYPES ###

# a_string = "this is a string of characters; they have no meaning to the programming language other than being a string of characters. Even the spaces are characters."
# a_number = 53
# another_number = 28
# print("lets do some math:", a_number + another_number)
#
# another_string = "53"
# print("we can't do math here, but lets 'add' these strings together:", another_string + "21")
# print("53 + 21 made 5321. It's not math, we just stuck the two strings of characters together")
# print("<-- this is a function; it runs code you can't see; when you run this script, it will print this string to the 'console'")
# print(a_string.upper(), "<-- this is just another function with a slightly different syntax, they it call a 'method' instead of a function."
#                          " Instead of upper(a_string), it is a_string.upper(). don't worry too much about this.")
#
# a_list = ["a list", "of strings", "with", "5", "entries"]
# stored_entry = a_list[2] #lists start with index 0, so this is the 3rd entry which will be "with"
# print("this should be the string 'with':", stored_entry)
# list_of_numbers = [2, 23, 94, -123, 10]
# print("94 + (-123):", list_of_numbers[2] + list_of_numbers[3])
# a_dictionary = {"dogs": 23, "zebras": 4, "bunnies": 10, "birds": 13} # A dictionary has key/value pairs
# print("how many zebraz?:", a_dictionary["zebras"])  # How we access to read an entry
# a_dictionary["monkies"] = 2 # How we write a new entry
# print(a_dictionary, "<-- monkies was added")
## an 'F-String' allows us to insert variables into the string
# print(f"I own {a_dictionary['dogs']} dogs, {a_dictionary['birds']}, birds, {a_dictionary['monkies']} monkeeees, and {a_dictionary['bunnies']} "
#       f"rabbits-- a total of {a_dictionary['dogs'] + a_dictionary['zebras'] + a_dictionary['bunnies'] + a_dictionary['birds'] + a_dictionary['monkies']}"
#       f" animals.")
#
## LOOPS ###
#
# loop_condition = 0
# while loop_condition < 20: # while-loop STAYS IN LOOP while condition is still true when check is done on this line. notice indentation on text line
# 	print(loop_condition)
# 	loop_condition = loop_condition + 1
#
## An 'Iterable' is a collection of things like a string (collection of characters), or list
# a for-loop iterates through an iterable. notice the variable 'blah_blah' changing every time through the loop.
# for blah_blah in "this string is a collection/iterable":
# 	print("variable blah_blah:", blah_blah)
# 	print("next")
#
# list_of_words = ["this", "zebra", "is", "a", "pretty", "boy"]
# print(list_of_words)
# for call_it_anything in list_of_words:
# 	if call_it_anything[0] in "zb":          #if index_0/first character is located in the collection(string in this case) "zb"
# 		print(call_it_anything.upper())
# 	else:
# 		print(call_it_anything)
#
## next we have a loop within a loop.
## the function "range()" can give us a series of numbers to be iterated-through
## len() gives length.
# for i in range(0, 50, 5):  # 0, up to (but not including) 50, by steps of 5
# 	for j in range(7):    # if we only supply a single number it, starts at 0 and runs up to (but not including) 7 in steps of 1
# 		print("i:", i, "j:", j)
#
## Notice below, len() is inside range(), so len() is resolved first, then the function range is called.
# stored_user_keystrokes = input("type some stuff please; Then press 'enter': ")
# print("you entered this many keystrokes", len(stored_user_keystrokes))
# for i in range(len(stored_user_keystrokes)):  #go through range of numbers based on length of stored_user_keystrokes
# 	print("keystroke number", i+1, ":", stored_user_keystrokes[i]) # keystrokes[index] remember the index starts at 0
	##notice that what we are printing many times is the variable 'i', and 'i' is changing (nothing special about the variable name)
	## != means 'is not equal', while == means 'is equal'
# added_names = []
# entry = input("give me a name or type 'stop': ")
# while entry.lower() != "stop":  # since 'stop' and 'STOP' are completely different characters, here i compare the guaranteed lowercase version with 'stop'
# 	added_names.append(entry)
# 	print(added_names)
# 	entry = input("give me a name or type 'stop': ")
# print("your names:", added_names)
#
### RECAP ###
# varable_is = "is a box to put stuff in"
# list_is = ["collection", "of", "stuff"] # each string is a collection of characters, so our list here is a collection of collections
# second_item = list_is[1]  # "of"
# dictionary_is = {"key" : "entry", "etc": 9999} # dictionaries are ordered, but keys are used for random access.
# access_dict = dictionary_is["etc"]  # 9999
# print(len(dictionary_is) + len(list_is))
# for current_string in list_is:
# 	print(current_string)
# 	for current_character in current_string:
# 		print(current_character)
# while input("type 'end' to end this loop; anything else to keep it going").lower() != "end":
# 	for i in range(10):
# 		print("caught in a loop")
# assign_to_this = "a string"
# if "this" == "THIS":
# 	assign_to_this = "true"
# else:
# 	assign_to_this = "false"
# print(assign_to_this)
#
### APPLICATION ###
## just need to add two more functions to the mix. we'll grab them from the python 'standard library':
# from random import randint  # randint gives us a random number in a range that we supply
# from time import sleep      # sleep allows us to pause for a given number of seconds
#
# hero_max_health = 25
# hero_health = hero_max_health
# hero_position = 0
# hero_attack = 6
# positions_per_area = 9
# damage_dealt = 0
# hero_healed = 0
# area = 0
# areas = 4
# enemy_health_refill = 6
# enemy_health = enemy_health_refill
# enemy_attack = 5
# print("the hero begins his journey across the treacherous planes, the imposing enemy stronghold hidden in the distance")
# sleep(2)
# while hero_health > 0 and area < areas:
# 	hero_position = hero_position + 1
# 	sleep(2)
# 	print(f"hero moves to mile {hero_position} of area {area}")
# 	if hero_position >= positions_per_area:     # greater-than or equal-to
# 		area = area + 1
# 		print("new area")
# 		hero_position = 0
# 		sleep(2)
# 		hero_healed = randint(1, 10)
# 		hero_health = hero_health + hero_healed
# 		if hero_health > hero_max_health:
# 			hero_health = hero_max_health
# 		print(f"hero rests and heals {hero_healed} points. hero now has {hero_health} health")
# 		sleep(2)
# 	else:   # else block only gets executed when the previous if block was not executed.
# 		if randint(1, 4) == 4:
# 			print("enemy encounter!")
# 			sleep(2)
# 			while hero_health > 0 and enemy_health > 0:  # fight loop
# 				damage_dealt = randint(0, hero_attack)
# 				if damage_dealt > 0:
# 					enemy_health = enemy_health - damage_dealt
# 					print(f"hero did {damage_dealt} damage to enemy. {enemy_health} enemy health remaining")
# 				else:
# 					print("hero missed")
# 				sleep(3)
# 				if enemy_health <= 0:        # less-than or equal-to
# 					print("enemy defeated")
# 				else:
# 					damage_dealt = randint(0, enemy_attack)
# 					if damage_dealt > 0:
# 						hero_health = hero_health - damage_dealt
# 						print(f"enemy did {damage_dealt} damage to hero. {hero_health} hero health remaining")
# 					else:
# 						print("enemy missed")
# 				sleep(3)
# 			print(f"hero's health is {hero_health}")
# 			enemy_health = enemy_health_refill
# if hero_health > 0:
# 	print("the hero rests at the precipice which overlooks the valley of the enemy stronghold; the story has just begun")
# else:
# 	print("like many others, the hero has fallen; he wasn't the first, and he won't be the last")
=======
from random import randint  ## randint gives us a random number in a range that we supply
from time import sleep      ## sleep allows us to pause for a given number of seconds

#hero_max_health = 25
#hero_health = hero_max_health
#hero_position = 0
#hero_attack = 6
#positions_per_area = 9
#damage_dealt = 0
#hero_healed = 0
#area = 0
#areas = 4
#enemy_health_refill = 6
#enemy_health = enemy_health_refill
#enemy_attack = 5
#print("the hero begins his journey across the treacherous planes, the imposing enemy stronghold hidden in the distance")
#sleep(2)
#while hero_health > 0 and area < areas:
#	hero_position = hero_position + 1#
#	sleep(2)
#	print(f"hero moves to mile {hero_position} of area {area}")
#	if hero_position >= positions_per_area:     # greater-than or equal-to
#		area = area + 1
#		print("new area")
#		hero_position = 0
#		sleep(2)
#		hero_healed = randint(1, 10)
#		hero_health = hero_health + hero_healed
#		if hero_health > hero_max_health:
#			hero_health = hero_max_health
#		print(f"hero rests and heals {hero_healed} points. hero now has {hero_health} health")
#		sleep(2)
#	else:   # else block only gets executed when the previous if block was not executed.
#		if randint(1, 4) == 4:
#			print("enemy encounter!")
#			sleep(2)
#			while hero_health > 0 and enemy_health > 0:  # fight loop
#				damage_dealt = randint(0, hero_attack)
#				if damage_dealt > 0:
#					enemy_health = enemy_health - damage_dealt
#					print(f"hero did {damage_dealt} damage to enemy. {enemy_health} enemy health remaining")
#				else:
#					print("hero missed")
#				sleep(3)
#				if enemy_health <= 0:        # less-than or equal-to
#					print("enemy defeated")
#				else:
#					damage_dealt = randint(0, enemy_attack)
#					if damage_dealt > 0:
#						hero_health = hero_health - damage_dealt
#						print(f"enemy did {damage_dealt} damage to hero. {hero_health} hero health remaining")
#					else:
#						print("enemy missed")
#				sleep(3)
#			print(f"hero's health is {hero_health}")
#			enemy_health = enemy_health_refill
#if hero_health > 0:
#	print("the hero rests at the precipice which overlooks the valley of the enemy stronghold; the story has just begun")
#else:
#	print("like many others, the hero has fallen; he wasn't the first, and he won't be the last")
>>>>>>> 25f6d630be3244f5d0f5c728826ac2c900b97717
