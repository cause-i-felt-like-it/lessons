### LESSON_01: WELCOME TO THE LOOP ###

# # let's create our own functions def. is the keyword for defining a function
# def function_name(argument_0, argument_1, argument_2):
# 	if argument_2 == "mul":
# 		result = argument_0 * argument_1
# 	elif argument_2 == "add":
# 		result = argument_0 + argument_1  #elif is else:if, if the above 'if' or 'elif' is a True, then the remaining elif's and else will be skipped
# 	elif argument_2 == "div":
# 		result = argument_0 / argument_1
# 	elif argument_2 == "sub":
# 		result = argument_0 - argument_1
# 	else:
# 		raise NameError(f"{argument_2} is an unsupported operation; check spelling.")
# 	return result
#
# # now lets use this function
# test_0 = function_name(21, 3, "add") # here 21 is argument_0, 3 is argument_1, and "add" is argument_2
# test_1 = function_name(21, 3, "sub")
# test_2 = function_name(21, 3, "div")
# test_3 = function_name(21, 3, "mul")
# print("test_0:", test_0, "test_1:", test_1, "test_2:", test_2, "test_3:", test_3)
# # test_4 = function_name(21, 3, "sqrt")  # (intentional error) check the console and look at the function's code above. Then re-comment this line.
#
# # I want to revisit the while-loop from last lesson, and connect it to the game Exa Punks. I'll insert the exaPunk instructions below.
# condition = 50
# current = 0
# while current < condition:
# 	#MARK EVALUATE
# 	# TEST current < condition
# 	# FJMP DONE_WITH_LOOP
# 	print(current)
# 	current += 1    # 'current += 1' is same as 'current = current + 1'
# 	# JUMP EVALUATE
# # MARK DONE_WITH_LOOP
# print("done", current)
#
# # Python actually translates into those exaPunk instructions (something like it). It's called Assembly language.
# # Assembly is linear just like the exaPunk instructions. These are the type of instructions our CPU needs: not python.
# # python is a 'high-level' language. Assembly is low-level. We won't be programming in Assembly any time soon ^_^
#
# # Class/Struct and objects/instances ###
# # later we're going to call this a struct, but for now it's a class (you'll understand later).
# # one of the reasons to do this is so i don't have to have a ton of separate variables, but can group them together.
# # we need an 'init' (initializer) function to help us create our object. I'm going to create a player.
# # self is the object being acted upon by the function (or 'method' as they are known when it comes to 'classes'
#
# class player:
# 	def __init__(self, given_name, given_health, given_attack):
# 		self.name = given_name
# 		self.max_health = given_health
# 		self.health = self.max_health
# 		self.attack = given_attack
#
# from random import randint  # from library module 'random', import this specific function.
# from time import sleep

# def fight(attacker, defender):
# 	damage_dealt = randint(0, attacker.attack)
# 	if damage_dealt > 0:
# 		defender.health = defender.health - damage_dealt
# 		print(f"{attacker.name} did {damage_dealt} damage to {defender.name}. {defender.name} has {defender.health} health remaining")
# 	else:
# 		print(f"{attacker.name} missed")
# 	sleep(2)
# 	return
##	#now we return back to where we were in our code
#
#
# def play_game(name, difficulty):
# 	area = 0
# 	areas = 4
# 	miles_per_area = 10
# 	mile = 0
# 	hero = player(name, 25, 8) # player is the class, and by writing this like a function call, we are calling the initializer we wrote above
# 	difficulty = int(difficulty) # int() here turns the string '1', '2', or '3', into the number(integer) 1, 2, or 3. if it was already integer it wil stay one.
# 	if difficulty == 1:
# 		enemy_max_attack = 4
# 		enemy_max_health = 5
# 	elif difficulty == 2:
# 		enemy_max_attack = 8
# 		enemy_max_health = 10
# 	elif difficulty == 3:  #we could just have 'else:' here instead of "elif difficulty == 3'
# 		enemy_max_attack = 12
# 		enemy_max_health = 15
# 	else:   #this else isn't needed if the code that calls play_game() function does the proper checking.
# 		raise ValueError(f"no such difficulty: {difficulty}")
# 	enemy_types = ["goblin", "imp", "dire wolf", "kobold", "basilisk"]  # when creating enemies we are going to go enemy_types[<number>] to retrieve a name
# 	print(f"{hero.name} begins his journey across the treacherous planes, the imposing enemy stronghold hidden in the distance")
# 	sleep(2)
# 	while hero.health > 0 and area < areas:
# 		mile += 1
# 		sleep(2)
# 		print(f"{hero.name} moves to mile {mile} of area {area}")
# 		if mile >= miles_per_area:
# 			area = area + 1
# 			print("new area")
# 			mile = 0
# 			sleep(2)
# 			hero_healed = randint(5, 10)
# 			hero.health = hero.health + hero_healed
# 			if hero.health > hero.max_health:
# 				hero.health = hero.max_health
# 			print(f"{hero.name} rests and heals {hero_healed} points. {hero.name} now has {hero.health} health")
# 			sleep(2)
# 		else:
# 			if randint(1, 4) == 4:
# 				print("enemy encounter!")
# 				##creating a new enemy with random stats and name every battle this time##
# 				enemy = player(given_name=enemy_types[randint(0,len(enemy_types)-1)], given_health=randint(4,enemy_max_health), given_attack=randint(1,enemy_max_attack))
# 				sleep(2)
# 				print(f"A {enemy.name} with {enemy.health} health and {enemy.attack} attack!")
# 				sleep(3)
# 				combatants = [hero, enemy]
# 				attacker_index = randint(0,1)
# 				defender_index = 1 - attacker_index   # 1 - 1 is 0. 1 - 0 is 1. we'll always get the fighter's index
# 				while hero.health > 0 and enemy.health > 0:  # fight loop
# 					fight(combatants[attacker_index], combatants[defender_index])
# 					if combatants[defender_index].health > 0:
# 						fight(combatants[defender_index], combatants[attacker_index])
# 	if hero.health > 0:
# 		print(f"{hero.name} rests at the precipice which overlooks the valley of the enemy stronghold; the story has just begun")
# 	else:
# 		print(f"like many others, {hero.name} has fallen; he wasn't the first, and he won't be the last")
# 	sleep(3)
# # remember the above code is just a function definition; we haven't called it yet
#
# play_again = "yes"
# chosen_difficulty = None
# chosen_name = ""
# while play_again in ["y", "yes"]:
# 	while chosen_difficulty not in ["1", "2", "3"]:
# 		chosen_difficulty = input("choose from difficulty 1, 2, or 3: ")
# 	while len(chosen_name) < 1:
# 		chosen_name = input("choose a name: ")
# 	play_game(chosen_name, chosen_difficulty)
# 	play_again = ""
# 	chosen_name = ""
# 	chosen_difficulty = ""
# 	while play_again not in ["yes", "no", "y", "n"]:
# 		play_again = input("do you want to play again?: ").lower()
## Make something of your own now! look over this and the last lesson for anything you missed.
## Use a search engine and/or youtube for anything you don't get! for example, you can just google 'python randint()' if you forget what randint() is.
## You can also lookup python classes on youtube. you'll find cool stuff. Don't be tied to just this resource. Become INDEPENDENT.
## The biggest lesson i can teach you is that YOU DON'T NEED ME. This is the point of my teaching style; you are able to glean from this code,
## your own realizations--you don't need me explaining every line to you in video form. You are clever enough! Trust yourself and keep digging!
## Some good python resources IF YOU WANT, are:
## -youtube video 'learn python - full course for beginners [tutorial]' with 25 million views.
## -the youtube channel: 'Corey Schafer' (especially if you're looking for more info on classes/objects)
## -www.realpython.com
## book on amazon 'Python and Algorithmic Thinking for the Complete Beginner (2nd Edition): Learn to Think Like a Programmer'
## Don't forget: there is a private discord for tutoring, which you can pay to enter via patreon!
## More python comin' at ya:
## See you in the next lesson