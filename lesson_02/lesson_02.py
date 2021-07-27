### LESSON_2: WELCOME TO THE GAME ###
## you might wonder what games have to do with embedded programming (the type of programming we are going to be doing. In
## in my opinion, it is the best preparation there is. Both games and embedded programming have strict performance
## demands and tight timing windows. In both we have an endless loop that needs to handle many events and tasks. Make sure you
## have downloaded the 2 image files for this lesson. Also make sure you install pygame, as shown in the video (or some other resource).

import pygame
from time import sleep
screen_size_x = 1300
screen_size_y = 100
BLUE = pygame.Color("blue")
BLACK = pygame.Color("black")
GREY = pygame.Color("grey")

### define function for removing a series of animation frames from a sprite strip and mirrored copies ###
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
		frame = pygame.transform.scale(frame, (128, 128))
		sprite_frames.append(frame)
		sprite_frames_mirrored.append(pygame.transform.flip(frame, True, False))
	return (sprite_frames, sprite_frames_mirrored)   # two return values

### create lists of animation frames by calling above function and storing the returned lists (two each call) ###
knight_idle_frames, knight_idle_frames_mirrored = extract_sprites(filename=r"sprites\KnightIdle_strip.png", width_height=(64,64), left_offset=2, interFrame_offset=64, num_of_frames=15)
knight_run_frames, knight_run_frames_mirrored = extract_sprites(filename=r"sprites\KnightRun_strip.png", width_height=(64,64), left_offset=18, interFrame_offset=96, num_of_frames=8)

animation_counter = 0
num_idle_frames = 15
num_running_frames = 8
x_pos = 0
accel = 0
max_accel = 2.5
speed = 0
max_speed = 35
speed_test = False
sprite_mirrored = False
pressed_keys = [] #list of keys that have been pressed but not released
pygame.display.init()
teh_display = pygame.display.set_mode((screen_size_x, screen_size_y))
playing = True
direction = 0
### GAME LOOP ###    there are 3 main sections of a game loop
while playing:
	### 1.capture user input ###    performance-wise this is a pretty trivial task
	for this_event in pygame.event.get():
		if this_event.type == pygame.KEYDOWN: # if event ia a pressed key
			if this_event.key == pygame.K_RIGHT:
				if "right" not in  pressed_keys: pressed_keys.append("right")
			elif this_event.key == pygame.K_LEFT:
				if "left" not in  pressed_keys: pressed_keys.append("left")
			elif this_event.key == pygame.K_ESCAPE:
				playing = False
		elif this_event.type == pygame.KEYUP: # if event is a released key
			if this_event.key == pygame.K_RIGHT:
				if "right" in pressed_keys:
					found_at = pressed_keys.index("right")
					del pressed_keys[found_at]
			elif this_event.key == pygame.K_LEFT:
				if "left" in pressed_keys:
					found_at = pressed_keys.index("left")
					del pressed_keys[found_at]
	### 2.simulate game world ###   this step requires much more heavy lifting, but it's nothing compared to step 3
	if pressed_keys:   # 'if variable' is shorthand for 'if variable not in [None, False, 0, "", [], {}]' in this case we are testing for [] (empty list)
		for key in pressed_keys: # process actions of keys that have not been released yet
			if key == "right":
				accel = max_accel
			elif key == "left":
				accel = (-max_accel)
			if accel > max_accel or accel < (-max_accel):
				accel = max_accel if accel > 0 else (-max_accel)    # search 'python ternary' to learn what this is
	else:
		accel = 0
		if speed: speed = int(speed-(max_accel/2)) if speed > 0 else int(speed+max_accel/2)         # search 'python ternary' to learn what this is
	if accel < 0 < speed or accel > 0 > speed:
		speed += accel*1.5
	else:
		speed += accel
	if speed > max_speed: speed = max_speed
	elif speed < (-max_speed): speed = (-max_speed)
	if sprite_mirrored and speed > 0: sprite_mirrored = False
	elif not sprite_mirrored and speed < 0: sprite_mirrored = True
	## 'if not sprite_mirrored' means 'if sprite_mirrored in [None, False, 0, "", [], {}]'. I could have said 'if sprite_mirrored == False', or 'if sprite_mirroed != True'
	x_pos += speed * 0.25
	if x_pos > (screen_size_x - 128):
		x_pos = screen_size_x - 128
		speed = 0
	elif x_pos < 0:
		x_pos = 0
		speed = 0
	### 3.render ###  in commercial releases, this step can get insanely complex, and can have tremendous performance requirements
	teh_display.fill(color=BLACK)
	if not speed:
		current_animation = knight_idle_frames if not sprite_mirrored else knight_idle_frames_mirrored
		num_animation_frames = num_idle_frames
	else:
		current_animation = knight_run_frames if not sprite_mirrored else knight_run_frames_mirrored
		num_animation_frames = num_running_frames
	if speed:
		animation_counter += abs(speed) * 0.02
	else:
		animation_counter += 0.2
	if animation_counter >= num_animation_frames: animation_counter = 0
	teh_display.blit(current_animation[abs(int(animation_counter))], (x_pos, 0))
	pygame.display.flip()
	sleep(0.04)
	## back to the top of the loop ##
print("quit")
pygame.display.quit()

## Don't take this as representative of the complexity of a real game. This is a toy demo on a toy language.


