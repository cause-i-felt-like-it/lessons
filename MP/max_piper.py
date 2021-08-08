### LESSON_2: WELCOME TO THE GAME ###
## you might wonder what games have to do with embedded programming (the type of programming we are going to be doing. In
## in my opinion, it is the best preparation there is. Both games and embedded programming have strict performance
## demands and tight timing windows. In both we have an endless loop that needs to handle many events and tasks. Make sure you
## have downloaded the 2 image files for this lesson. Also make sure you install pygame, as shown in the video (or some other resource).

import pygame
from time import sleep
screen_size_x = 1500
screen_size_y = 300
CUSTOM_COLOR = (79, 122, 74, 255)
class Player(object):
	def __init__(self, slowdown,max_accel, max_walk_speed, max_run_speed, idle_frames, walk_frames, run_frames):
		self.max_accel = max_accel
		self.slowdown = slowdown
		self.max_run_speed = max_run_speed
		self.max_walk_speed = max_walk_speed
		self.idle_frames = idle_frames
		self.walk_frames = walk_frames
		self.run_frames = run_frames
		self.ani_counter = 0
		self.x_pos = 0
		self.speed = 0
		self.accel = 0
		self.current_frame = None
		self.mirrored = False
		self.running = False
		self.last_speed = 0
		self.run_change = False
		self.run_array = None
		self.run_mirrored_array = None
		self.walk_array = None
		self.walk_mirrored_array = None
		self.idle_array = None
		self.idle_mirrored_array = None
		self.last_ani_counter = 0
		self.current_array = None
		self.last_run = False

Max = Player(max_accel=2, max_walk_speed=4, max_run_speed=12, idle_frames=55, walk_frames=6, run_frames=4, slowdown=4)
Piper = Player(max_accel=2, max_walk_speed=6, max_run_speed=6, idle_frames=15, walk_frames=14, run_frames=14, slowdown=3)
players = [Max, Piper]

def extract_sprites(filename: str, width_height: tuple, left_offset: int, interFrame_offset: int, num_of_frames: int) -> (list, list):
	sprite_file = open(rf"{filename}")
	sprite_sheet = pygame.image.load(sprite_file)
	sprite_file.close()
	sprite_frames = []
	sprite_frames_mirrored = []
	for column in range(0,num_of_frames):
		temp_pos_x =  left_offset+(column*interFrame_offset)
		temp_rect = pygame.Rect((temp_pos_x,0, width_height[0], width_height[1]))
		frame = pygame.Surface(temp_rect.size, flags=pygame.SRCALPHA)
		frame.blit(sprite_sheet, (0, 0), temp_rect)
		frame = pygame.transform.scale(frame, (256, 256))
		sprite_frames.append(frame)
		sprite_frames_mirrored.append(pygame.transform.flip(frame, True, False))
	return (sprite_frames, sprite_frames_mirrored)   # two return values

max_idle_frames, max_idle_frames_mirrored = extract_sprites(filename=r"sprites\max_idle-Sheet.png", width_height=(32,32), left_offset=0, interFrame_offset=32, num_of_frames=Max.idle_frames)
max_walk_frames, max_walk_frames_mirrored = extract_sprites(filename=r"sprites\max_walk-Sheet.png", width_height=(32,32), left_offset=0, interFrame_offset=32, num_of_frames=Max.walk_frames)
max_run_frames, max_run_frames_mirrored = extract_sprites(filename=r"sprites\max_run-Sheet.png", width_height=(32,32), left_offset=0, interFrame_offset=32, num_of_frames=Max.run_frames)
Max.idle_array = max_idle_frames
Max.idle_mirrored_array = max_idle_frames_mirrored
Max.walk_array = max_walk_frames
Max.walk_mirrored_array = max_walk_frames_mirrored
Max.run_array = max_run_frames
Max.run_mirrored_array = max_run_frames_mirrored
Max.current_array = Max.idle_array
Max.current_frame = Max.current_array[Max.ani_counter]
piper_idle_frames, piper_idle_frames_mirrored = extract_sprites(filename=r"sprites\piper_idle-Sheet.png", width_height=(32,32), left_offset=0, interFrame_offset=32, num_of_frames=Piper.idle_frames)
piper_walk_frames, piper_walk_frames_mirrored = extract_sprites(filename=r"sprites\piper_skip-Sheet.png", width_height=(32,32), left_offset=0, interFrame_offset=32, num_of_frames=Piper.walk_frames)
piper_run_frames, piper_run_frames_mirrored = extract_sprites(filename=r"sprites\piper_skip-Sheet.png", width_height=(32,32), left_offset=0, interFrame_offset=32, num_of_frames=Piper.run_frames)
Piper.idle_array = piper_idle_frames
Piper.idle_mirrored_array= piper_idle_frames_mirrored
Piper.walk_array = piper_walk_frames
Piper.walk_mirrored_array = piper_walk_frames_mirrored
Piper.run_array = piper_run_frames
Piper.run_mirrored_array = piper_run_frames_mirrored
Piper.current_array = Piper.idle_array
Piper.current_frame = Piper.current_array[Piper.ani_counter]

pressed_keys = []
pygame.display.init()
teh_display = pygame.display.set_mode((screen_size_x, screen_size_y))
playing = True
direction = 0
while playing:
	Max.accel = 0
	Piper.accel = 0
	Max.running = False
	for this_event in pygame.event.get():
		if this_event.type == pygame.KEYDOWN:
			if this_event.key == pygame.K_RIGHT:
				if "piper_right" not in  pressed_keys: pressed_keys.append("piper_right")
			elif this_event.key == pygame.K_LEFT:
				if "piper_left" not in  pressed_keys: pressed_keys.append("piper_left")
			elif this_event.key == pygame.K_d:
				if "max_right" not in pressed_keys: pressed_keys.append("max_right")
			elif this_event.key == pygame.K_a:
				if "max_left" not in pressed_keys: pressed_keys.append("max_left")
			elif this_event.key == pygame.K_ESCAPE:
				playing = False
			elif this_event.key == pygame.K_SPACE:
				if "max_run" not in pressed_keys: pressed_keys.append("max_run")
		elif this_event.type == pygame.KEYUP:
			if this_event.key == pygame.K_RIGHT:
				if "piper_right" in pressed_keys:
					found_at = pressed_keys.index("piper_right")
					del pressed_keys[found_at]
			elif this_event.key == pygame.K_LEFT:
				if "piper_left" in pressed_keys:
					found_at = pressed_keys.index("piper_left")
					del pressed_keys[found_at]
			elif this_event.key == pygame.K_d:
				if "max_right" in pressed_keys:
					found_at = pressed_keys.index("max_right")
					del pressed_keys[found_at]
			elif this_event.key == pygame.K_a:
				if "max_left" in pressed_keys:
					found_at = pressed_keys.index("max_left")
					del pressed_keys[found_at]
			elif this_event.key == pygame.K_SPACE:
				if "max_run" in pressed_keys:
					found_at = pressed_keys.index("max_run")
					del pressed_keys[found_at]
	if pressed_keys:
		for key in pressed_keys:
			if key == "max_right":
				Max.accel = Max.max_accel
			elif key == "max_left":
				Max.accel = (-Max.max_accel)
			elif key == "piper_right":
				Piper.accel = Piper.max_accel
			elif key == "piper_left":
				Piper.accel = (-Piper.max_accel)
			elif key == "max_run":
				Max.running = True
	for player in players:
		if not player.accel:
			if player.speed > 0:
				if player.speed < player.slowdown:
					player.speed = 0
				else:
					player.speed -= player.slowdown
			elif player.speed < 0:
				if player.speed > player.slowdown: player.speed = 0
				else: player.speed += player.slowdown
		elif not player.running:
			if player.speed > player.max_walk_speed:
				player.speed -= player.slowdown
			elif player.speed < (-player.max_walk_speed):
				player.speed += player.slowdown
			else:player.speed += player.accel
		else:
			player.speed += player.accel
		if player.speed > player.max_run_speed: player.speed = player.max_run_speed
		elif player.speed < (-player.max_run_speed): player.speed = (-player.max_run_speed)
		if player.last_speed > 0 >= player.speed or player.last_speed < 0 <= player.speed or not player.last_speed and player.speed or player.last_run != player.running:
			player.ani_counter = 0
			if  player.speed > 0:
				player.mirrored = False
				if player.running:
					player.current_array = player.run_array
				else: player.current_array = player.walk_array
			elif player.speed < 0:
				player.mirrored = True
				if player.running: player.current_array = player.run_mirrored_array
				else: player.current_array = player.walk_mirrored_array
			elif not player.speed:
				player.current_array = player.idle_array
			player.current_frame = player.current_array[int(player.ani_counter)]
	teh_display.fill(color=CUSTOM_COLOR)
	if Max.speed:
		Max.ani_counter += abs(Max.speed) * 0.05 if not Max.running else abs(Max.speed) * 0.02
		if Max.running and Max.ani_counter >= Max.run_frames: Max.ani_counter = 0
		elif not Max.running and Max.ani_counter >= Max.walk_frames: Max.ani_counter = 0
	else:
		Max.ani_counter += 0.25
		if Max.ani_counter >= Max.idle_frames:
			Max.ani_counter =0
	if Piper.speed:
		Piper.ani_counter += abs(Piper.speed) * 0.05
		if Piper.ani_counter >= Piper.run_frames: Piper.ani_counter = 0
	else:
		Piper.ani_counter += 0.1
		if Piper.ani_counter >= Piper.idle_frames:
			Piper.ani_counter = 0
	for player in players:
		if player.x_pos > (screen_size_x -180):
			player.x_pos = screen_size_x -180
			player.speed = 0
			player.accel = 0
			player.ani_counter = 0
			player.current_array = player.idle_array
			player.current_frame = player.current_array[player.ani_counter]
			player.run = False
		elif player.x_pos < -80:
			player.x_pos = -80
			player.speed = 0
			player.accel = 0
			player.ani_counter = 0
			player.current_array = player.idle_array
			player.current_frame = player.current_array[player.ani_counter]
			player.run = False
	Max.x_pos += Max.speed
	Piper.x_pos += Piper.speed
	if Piper.ani_counter % 1 < Piper.last_ani_counter % 1: Piper.current_frame =  Piper.current_array[int(Piper.ani_counter)]
	if Max.ani_counter % 1 < Max.last_ani_counter % 1: Max.current_frame =  Max.current_array[int(Max.ani_counter)]
	teh_display.blit(Piper.current_frame, (Piper.x_pos, 25))
	teh_display.blit(Max.current_frame, (Max.x_pos, 25))
	pygame.display.flip()
	sleep(0.04)
	for player in players:
		player.last_ani_counter = player.ani_counter
		player.last_speed = player.speed
		player.last_run = player.running
print("quit")
pygame.display.quit()



