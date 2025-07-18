#Author: Jhan Gomez <br>
#Date: 07-19-2025, 2:10 PM EST  <br>
#Version (Pre-Release): 1.0.9 <br>
#Purpose: To make a fun game in PyGame that also demonstrates my understanding of python such as libraries, loops, conditionals, branching, front-end graphics, back-end code, and more.  <br>
#DONE: Controls screen, Bull movement across the x axis, bull drawing, item spawning and respawning logic, points accumulated, player when stationary, player when jumping, windows scaling set to 100%, bgm (select), out of bounds, warn and projectile system. <br>
#Fully complete bull and item logic, store, game over
#Item and enviroemental hazard, splash screen, ground, high score + time and name to file, partial(animation for background)
#To-Draw: player when moving. <br>
#To-Do and IDEAS:  <br> 
#Story sequence needed, aswell as mission accomplished screen. Potentially, down the line, will add second mode where you get a certain amount of time
#to get the items, sort of like the original vision. This mode will be a countdown where you can get unlimited items in a certain time frame, with a 1 minute, 5 minute, 15 minute, etc modes.


#For water hazard.
#Show warning symbol like exclamation point similar to loot respawn logic.
#Then have a seperate countdown withing that calls the function to draw the water, and remove the warning sign no sprites for this one.
import ctypes #These two lines of code were found out to be needed when I attempted to draw an image on the background for the game over.
#It is called ctypes, which interacts with the windows API, which is crucial because windows has scaling set to 125% as a default.
ctypes.windll.user32.SetProcessDPIAware() #Makes windows not use its own scaling configs and instead use pygames which is ideal for better and faster development
#aswell as placements.
import pygame #Pygame library is imported in.
from pygame import mixer #This is the music package from pygame that is being imported.
from sys import exit #Exit is imported from the os.
from tkinter import * #Imports the entire tkinter module
from tkinter import ttk #Imports the ttk submodule.
import random #Random module imported in.
import datetime #Important for the leaderboard
pygame.init() #Pygame is initialized.
SCREEN_WIDTH=1920 #Screen width is set to be 1920
SCREEN_HEIGHT=1080 #Screen height is set to be 1080.
return_pressed=0 #Determines how many times return was pressed.
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #The dimensions are now set to be the displays dimensions.
game_active=False #This boolean allows pausing for when the player either wins or looses.
clock=pygame.time.Clock() #Allows a consistent frame rate in my game.
font=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 100) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
font_2=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 50) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
font_3=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 75) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
font_4=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 40) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
font_5=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 20) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
font_6=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 35) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
starting_time=pygame.time.get_ticks() #Used for the timer.
starting_time_secs=pygame.time.get_ticks() #Used for the timer in seconds.
#Sprites for animationms
controls=pygame.image.load('Game_Files/Assets/Stage/Controls_KBM.png').convert_alpha() #Screen showing the controls is loaded in.
controls_location=controls.get_rect(topleft=(0,0)) #The location of the controls
disclaimer=pygame.image.load('Game_Files/Assets/Stage/disclaimer.png').convert_alpha() #Loads the disclaimer in.
disclaimer_location=disclaimer.get_rect(topleft=(0,0)) #Puts the disclaimer on screen.
player_walking_1=pygame.image.load('Game_Files/Assets/Humans/player_stationary.png').convert_alpha() #Asset loaded in, convert alpha helps it have the higest quality.
player_walking_2=pygame.image.load('Game_Files/Assets/Humans/player_stationary.png').convert_alpha() #Asset loaded in, convert alpha helps it have the higest quality.
player_walking=[player_walking_1, player_walking_2] #Has two sprites, can be changed.
player_walking_index=0 #Allows one of the above indexes to be selected to animate
player_256=player_walking[player_walking_index] #The sprite chosen is the one at the specified index position within the array.
player_hitbox = player_256.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 45)) #Works regardless of screen size chosen.
player_jumping=pygame.image.load('Game_Files/Assets/Humans/player_jumping.png').convert_alpha() #Jumping animation for player.
shop=pygame.image.load('Game_Files/Assets/Stage/jewel-shop.png').convert_alpha() #Loads the shops background in.
shop_location=shop.get_rect(topleft=(0,0)) #Puts the shop at this location.
#Add special loot, cooldown, current time, add final time to game over screen, mechanics at a glance.

#Frames for background splash screen.
frame_1=pygame.image.load("Game_Files/Assets/Story/FRAME_1.png").convert_alpha()
frame_2=pygame.image.load("Game_Files/Assets/Story/FRAME_2.png").convert_alpha()
frame_3=pygame.image.load("Game_Files/Assets/Story/FRAME_3.png").convert_alpha()
frame_4=pygame.image.load("Game_Files/Assets/Story/FRAME_4.png").convert_alpha()
frame_5=pygame.image.load("Game_Files/Assets/Story/FRAME_5.png").convert_alpha()
frame_6=pygame.image.load("Game_Files/Assets/Story/FRAME_6.png").convert_alpha()
frame_7=pygame.image.load("Game_Files/Assets/Story/FRAME_7.png").convert_alpha()
frame_8=pygame.image.load("Game_Files/Assets/Story/FRAME_8.png").convert_alpha()
frame_9=pygame.image.load("Game_Files/Assets/Story/FRAME_9.png").convert_alpha()
frame_10=pygame.image.load("Game_Files/Assets/Story/FRAME_10.png").convert_alpha()
frame_11=pygame.image.load("Game_Files/Assets/Story/FRAME_11.png").convert_alpha()
frame_12=pygame.image.load("Game_Files/Assets/Story/FRAME_12.png").convert_alpha()
frame_13=pygame.image.load("Game_Files/Assets/Story/FRAME_13.png").convert_alpha()
frame_14=pygame.image.load("Game_Files/Assets/Story/FRAME_14.png").convert_alpha()
frame_15=pygame.image.load("Game_Files/Assets/Story/FRAME_15.png").convert_alpha()
frame_16=pygame.image.load("Game_Files/Assets/Story/FRAME_16.png").convert_alpha()
frame_17=pygame.image.load("Game_Files/Assets/Story/FRAME_17.png").convert_alpha()
frame_18=pygame.image.load("Game_Files/Assets/Story/FRAME_18.png").convert_alpha()
frame_19=pygame.image.load("Game_Files/Assets/Story/FRAME_19.png").convert_alpha()
frame_20=pygame.image.load("Game_Files/Assets/Story/FRAME_20.png").convert_alpha()
frame_21=pygame.image.load("Game_Files/Assets/Story/FRAME_21.png").convert_alpha()
frame_22=pygame.image.load("Game_Files/Assets/Story/FRAME_22.png").convert_alpha()
frame_23=pygame.image.load("Game_Files/Assets/Story/FRAME_23.png").convert_alpha()
frame_24=pygame.image.load("Game_Files/Assets/Story/FRAME_24.png").convert_alpha()
frame_25=pygame.image.load("Game_Files/Assets/Story/FRAME_25.png").convert_alpha()
frame_26=pygame.image.load("Game_Files/Assets/Story/FRAME_26.png").convert_alpha()
frame_27=pygame.image.load("Game_Files/Assets/Story/FRAME_27.png").convert_alpha()
frame_28=pygame.image.load("Game_Files/Assets/Story/FRAME_28.png").convert_alpha()
frame_29=pygame.image.load("Game_Files/Assets/Story/FRAME_29.png").convert_alpha()
frame_30=pygame.image.load("Game_Files/Assets/Story/FRAME_30.png").convert_alpha()
frame_31=pygame.image.load("Game_Files/Assets/Story/FRAME_31.png").convert_alpha()
frame_32=pygame.image.load("Game_Files/Assets/Story/FRAME_32.png").convert_alpha()
frame_33=pygame.image.load("Game_Files/Assets/Story/FRAME_33.png").convert_alpha()
frame_34=pygame.image.load("Game_Files/Assets/Story/FRAME_34.png").convert_alpha()
frame_35=pygame.image.load("Game_Files/Assets/Story/FRAME_35.png").convert_alpha()
frame_36=pygame.image.load("Game_Files/Assets/Story/FRAME_36.png").convert_alpha()
frame_37=pygame.image.load("Game_Files/Assets/Story/FRAME_37.png").convert_alpha()
frame_38=pygame.image.load("Game_Files/Assets/Story/FRAME_38.png").convert_alpha()
frame_39=pygame.image.load("Game_Files/Assets/Story/FRAME_39.png").convert_alpha()
frame_40=pygame.image.load("Game_Files/Assets/Story/FRAME_40.png").convert_alpha()
frame_41=pygame.image.load("Game_Files/Assets/Story/FRAME_41.png").convert_alpha()
frame_42=pygame.image.load("Game_Files/Assets/Story/FRAME_42.png").convert_alpha()
frame_43=pygame.image.load("Game_Files/Assets/Story/FRAME_43.png").convert_alpha()
pic_1=pygame.image.load("Game_Files/Assets/Stage/CC_BY_NA_SA_4_enter.png").convert_alpha()
pic_2=pygame.image.load("Game_Files/Assets/Stage/CC_BY_NA_SA_4_no_enter.png").convert_alpha()
breakdown_1=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-1.png").convert_alpha()
breakdown_2=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-2.png").convert_alpha()
breakdown_3=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-3.png").convert_alpha()
breakdown_4=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-4.png").convert_alpha()
breakdown_5=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-5.png").convert_alpha()
breakdown_6=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-6.png").convert_alpha()
breakdown_7=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-7.png").convert_alpha()
breakdown_8=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-8.png").convert_alpha()
breakdown_9=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-9.png").convert_alpha()
breakdown_10=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-10.png").convert_alpha()
breakdown_11=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-11.png").convert_alpha()
breakdown_12=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-12.png").convert_alpha()
breakdown_13=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-13.png").convert_alpha()
breakdown_14=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-14.png").convert_alpha()
breakdown_15=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-15.png").convert_alpha()
breakdown_16=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-16.png").convert_alpha()
breakdown_17=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-17.png").convert_alpha()
breakdown_18=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-18.png").convert_alpha()
breakdown_19=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-19.png").convert_alpha()
breakdown_20=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-20.png").convert_alpha()
breakdown_21=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-21.png").convert_alpha()
breakdown_22=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-22.png").convert_alpha()
breakdown_23=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-23.png").convert_alpha()
breakdown_24=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-24.png").convert_alpha()
breakdown_25=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-25.png").convert_alpha()
breakdown_26=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-26.png").convert_alpha()
breakdown_27=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-27.png").convert_alpha()
breakdown_28=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-28.png").convert_alpha()
breakdown_29=pygame.image.load("Game_Files/Assets/Story/Pre-Breakdown-28-No-Text.png").convert_alpha()
breakdown_30=pygame.image.load("Game_Files/Assets/Story/new-breakdown.png").convert_alpha()
ominous_1=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance.png").convert_alpha()
ominous_2=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-2.png").convert_alpha()
ominous_3=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-3.png").convert_alpha()
ominous_4=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-4.png").convert_alpha()
ominous_5=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-5.png").convert_alpha()
ominous_6=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-6.png").convert_alpha()
ominous_7=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-7.png").convert_alpha()
ominous_8=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-8.png").convert_alpha()
ominous_9=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-9.png").convert_alpha()
ominous_10=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-10.png").convert_alpha()
ominous_11=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-11.png").convert_alpha()
ominous_12=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-12.png").convert_alpha()
ominous_13=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-13.png").convert_alpha()
ominous_14=pygame.image.load("Game_Files/Assets/Story/bull-first-appearance-14.png").convert_alpha()
background_rolling=[frame_1, frame_2, frame_3, 
                    frame_4, frame_5, frame_6, 
                    frame_7, frame_8, frame_9, 
                    frame_10, frame_11, frame_12, 
                    frame_13, frame_14, frame_15, 
                    frame_16, frame_17, frame_18, 
                    frame_19, frame_20, frame_21, 
                    frame_22, frame_23, frame_24, 
                    frame_25, frame_26, frame_27, 
                    frame_28, frame_29, frame_30,
                    frame_31, frame_32, frame_33,
                    frame_34, frame_35, frame_36,
                    frame_37, frame_38, frame_39,
                    frame_40, frame_41, frame_42] # I need a totaL minimum  of 16 for smooth animation.
background_index=0 #The index for which frame to pick is set to 0.
background=background_rolling[background_index] #The background is set to be the index position of the background index withing the background rolling list.
background_location=background.get_rect(topleft=(0,0)) #Draws the background at this location.
flashing_rolling=[pic_1, pic_2] #Contains the pictures for the CC BY NA SA 4 Disclaimer
flashing_index=0 #Contains the index for the disclaimer cc.
flashing=flashing_rolling[flashing_index] #Picks which picture to display depending on the index.
flashing_location=flashing.get_rect(topleft=(0,0)) #Displays the CC disclaimer on the screen.
breakdown_rolling=[breakdown_1, breakdown_2, breakdown_3, breakdown_4, 
                   breakdown_5, breakdown_6, breakdown_7, breakdown_8, 
                   breakdown_9, breakdown_10, breakdown_11,breakdown_12, 
                   breakdown_13, breakdown_14, breakdown_15, breakdown_16, 
                   breakdown_17, breakdown_18, breakdown_19, breakdown_20, breakdown_21,
                   breakdown_22, breakdown_23, breakdown_24, breakdown_25, 
                   breakdown_26, breakdown_27, breakdown_28]
breakdown_index=0 #The index for which frame to pick is set to 0.
breakdown=breakdown_rolling[breakdown_index] #The background is set to be the index position of the breakdown index within the breakdown rolling list.
breakdown_location=breakdown.get_rect(topleft=(0,0)) #Draws the background at this locatio
breakdown_warning_rolling=[breakdown_28, breakdown_29] #Contains the pictures for the breakdown warning.
breakdown_warning_index=0  #The index for which frame to pick is set to 0.
breakdown_warning=breakdown_warning_rolling[breakdown_warning_index] #The background is set to be the index position of the breakdown warning index within the breakdown warning rolling list.
breakdown_warning_location=breakdown_warning.get_rect(topleft=(0,0)) #Draws the background at this locatio
bull_first_appearance_rolling=[ominous_1, ominous_2, ominous_3, ominous_4,
                               ominous_5, ominous_6, ominous_7, ominous_8,
                               ominous_9, ominous_10, ominous_11, ominous_12,
                               ominous_13, ominous_14]
bull_first_appearance_index=0 #The index for which frame to pick is set to 0.
bull_first_appearance=bull_first_appearance_rolling[bull_first_appearance_index] #picks an image to display
bull_first_appearance_location=bull_first_appearance.get_rect(topleft=(0,0)) #Places the image on the screen.
def leaderboard_function(): #A function to display scores of users.
      root = Tk() #Root is set to the main window where everything else will be attached
      root.title("A Bull In A China Shop") #A title is set for the program.
      with open ("Scoreboard.txt", "r") as file: #Opens the scoreboard file.
         scores=file.read() #Reads the text from the file with the appropriate line spacing.
      frame = ttk.Frame(root) #A frame is made using the .Frame method and will be attached to root.
      frame.pack(fill=BOTH, expand=True, padx=10, pady=10) #This frame will fill from both left and right, will expand if necessaring and will have x and y spacing of 10.
      scrollbar = ttk.Scrollbar(frame)  #A scrollbar is implemented using ttk's.scrollbar method on the frame.
      scrollbar.pack(side=RIGHT, fill=Y) #The scrollbar will be on the right side, with control of the Y axis.
      text_widget = Text(frame, wrap=NONE, yscrollcommand=scrollbar.set, height=15, width=50) # Text will be passed on to the frame, with vertical scrolling and a height and width for the text area.
      text_widget.insert(END, scores) #Text is added after the last characther, scores will be this text.
      text_widget.pack(side=LEFT, fill=BOTH, expand=True) #Puts the text to the left side, fills the textbox from both sides, and will expand if necessary.
      text_widget.config(state=DISABLED) #This prevents the player from typing in junk values.
      root.mainloop() #handles events
#Sprites for player!
def player_sprites(): #Function for sprites, based of https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=10153s&ab_channel=ClearCode
    global player_256, player_walking_index #player_256 and player_walking_index must be declared at globally.
    if player_hitbox.bottom < starting_pos: #If the player is above a certain y position, then the jumpinh animation must be drawn.
       player_256=player_jumping #Player jumping is made to be the image drawn on the screen.
    else: #Otherwise, the player must be on the ground
       player_walking_index+=0.1 #Slowly swaps frames between 0 and  1 for smooth movement.
       if player_walking_index >= len(player_walking): #Prevents an out of bounds exception.
          player_walking_index=0 #Index is reset to 0.
       player_256=player_walking[int(player_walking_index)] #The loop restarts   
game_over_screen=pygame.image.load('Game_Files/Assets/Stage/Game_Over.png').convert_alpha() #Game over screen loaded in when drawn.
game_over_draw=game_over_screen.get_rect(topleft=(0, 0)) #Location of game over screen declared.
#Assets and Locations
item=pygame.image.load('Game_Files/Assets/Interactable/Necklace-2.png').convert_alpha() #Necklace asset loaded in.
goal=0 #Goal is set to be a default of 0
goal_input = "" #Gets the users desired score
player_speed=0 #Default player speed is set to 0.
player_gravity=0 #Player gravity is set to 0.
special_speed_counter=3 #Allows the player to use a special dash for a total of 3 times.
starting_pos=player_hitbox.y #The starting pos of the player is set to the initial y location of the player.
item_last_seen=pygame.time.get_ticks() #Stores the last time the item was seen.
item_respawn_cooldown=random.randint(2000,5000) #A cooldown of between 3 and 5 seconds is made.
item_x_pos=random.randint(300,1581) #Default x value range for normal items
item_y_pos=random.randint(500,600) #Default y valur range for normal items.
item_hitbox=item.get_rect(topleft=(item_x_pos, item_y_pos)) #The item is placed at the randomly generated x and y positions.
points=0 #Points counter, default is 0.
points_text=font_2.render("Points: 0 ", True, "Black") #At the beggining, the score is 0 and that is displayed on the screen.
points_text_box=points_text.get_rect(topleft=(0, 0)) #Sets the points location on the screen.
bull=pygame.image.load('Game_Files/Assets/Bull/bull_256.png') #Loads the bull asset. Imagee will change depending on whether the bull is moving left or right.
bull_hitbox=bull.get_rect(midbottom=(SCREEN_WIDTH-129, SCREEN_HEIGHT-45)) #Bull is placed at specific location on the screen.
bull_starting_pos=bull_hitbox.y #Bull's starting position is stored for later gravitational calculations.
bull_last_seen=pygame.time.get_ticks() #the last time the bull was seen is set to this time.
bull_movement_cooldown=random.randint(1000,2000) #The default cooldown 
bull_speed=0 #The default bull speed is set to 0.
bull_gravity=0 #The default bull gravity is set to 0.
inner_loop_x=False #inner_loop_x is set to false as a default, but will be changed later.
inner_loop_y=False #Same as above, but for the y axis.
bull_charging=False #The bull is by default not charging so this is set to false.
main_game=False #The main game is set to false as a default.
splash_screen=True #The splash screen is true by default.
goal_stored=0 #The goal stored is 0 by default.
game_over=False #The game is not over by default.
total_time="" #Stores the total time used, blank by default.
set_name=False #Set name is set to false by default.
#Water puddle hazard and drawing on screen.
animation_active=True #Flag to handle the animation of the splash screen.
water_puddle=pygame.image.load('Game_Files/Assets/Interactable/water-test.png').convert_alpha() #Picture loaded in as water_puddle
water_puddle_2=pygame.image.load('Game_Files/Assets/Interactable/water-test-2.png').convert_alpha() #Loads in a second water puddle.
water_possible_locations=[0, 393] #Possible locations for the water puddle.
water_possible_locations_2=[785, SCREEN_WIDTH-350] #Possible locations for the water puddle.
water_location_select=random.choice(water_possible_locations) #Selects a location to choose from for the water.
water_location_select_2=random.choice(water_possible_locations_2) #Places the second water puddle at these locations.
water_puddle_x=water_location_select #Water puddle can appear at these locations at the x axis 
water_puddle_y=starting_pos - 110 #Water puddle y is always set to this locations
water_puddle_location=water_puddle.get_rect(topleft=(water_puddle_x, water_puddle_y)) #The water hazard is drawn at this location.
water_puddle_x_2=water_location_select_2 #Water puddle can appear at these locations at the x axis 
water_puddle_y_2=starting_pos - 110 #Water puddle y is always set to this locations
water_puddle_location_2=water_puddle.get_rect(topleft=(water_puddle_x_2, water_puddle_y_2)) #The water hazard is drawn at this location.
water_puddle_cooldown=random.randint(5000,10000) #The water hazard will be redrawn every 5 to 10 seconds.
water_puddle_last_seen=pygame.time.get_ticks() #Will check when the water puddle was last seen.
score=0 #Score is by default set to 0.
set_score=False #This flag determines whether or not the user can input the score
time_keep=False #this flag determines whether the timer is active, useful for when game over or mission accomplished.
mixer.init() #Needed for music and sfx later on.
projectile=pygame.image.load("Game_Files/Assets/Interactable/Danger.png").convert_alpha() #Loads in the projectile image.
warning=pygame.image.load("Game_Files/Assets/Interactable/Warning.png").convert_alpha() #Loads in the warning image.
warning_active=False # A flag used to see if the warning is active is made.
warn_window=5000 #The user will get 5 seconds to react to the projectile
warning_x=0 #Warning x is initally set to 0.
warning_y=random.randint(0,450) #Warning y is initially set to 0.
projectile_x=warning_x #projectile x is set to warning x.
projectile_y=warning_y #Projectile y is set to warning y.
projectile_location=projectile.get_rect(topleft=(projectile_x, projectile_y)) #Puts the projectile at the location of projectile x and projectile y.
warning_location=warning.get_rect(topleft=(warning_x, warning_y)) #Warning is set to the location of warning x and warning  y.
projectile_active=False #This flag is used to see if the projectile should be launched.
projectile_last_seen=pygame.time.get_ticks() #A timer is used to see when the projectile was last seen.
projectile_cooldown=random.randint(5000,7000) #A cooldown determines how much time should pass before the projectile is shown on the screen.
warning_last_seen=pygame.time.get_ticks() #used to see when the warning was last seen.
warning_checked=0 #Warning checked is used to check the time once, against the warn window.
#Reworked, allows for story to be drawn in.
special=font_4.render("Dashes remaining: " + str(special_speed_counter), True, 'Black') #Tells how many dashes the player has to use.
special_location=special.get_rect(topleft=(475,0)) #Draws the amount of dashes to the screen.
py_made=pygame.image.load('Game_Files/Assets/Stage/pygame_powered.png').convert_alpha() # loads pygame powered image
py_location=py_made.get_rect(topleft=(0,0)) #Draws the powered by pygame image on screen.
name_input="" #Stores the user's name.
attempted_score="" #Stores the user's attempted score.
success=False #By default, the user did not succeed.
def screen_to_take_you_to(): #A function handles which screen is drawn.
      global set_name, controls, controls_location, breakdown_location, breakdown_warning_location, breakdown_warning, breakdown_warning_index #set score is set at the global level.
      global background, background_index, flashing_index, flashing, breakdown, breakdown_index, bull_first_appearance, bull_first_appearance_index, bull_first_appearance_location #background, background_index, flashing, and flashing index also declared  globally.
      if return_pressed == 0: #If return pressed is less than 0, then this will run.
         screen.fill((0,0,0)) #Screen filled with black
         screen.blit(py_made, py_location) #pygame screen drawn to the screen.
      elif return_pressed==1: #If return pressed is equal to 1, then this will run.
         screen.fill((0,0,0)) #Screen filled with black to get rid of previous input.
         screen.blit(disclaimer,disclaimer_location) #Disclaimer drawn to screen.
      elif return_pressed==2: #If return pressed is equal to two, then this will run.
         flashing_index+=0.005 #Flashes the CC BY NA SA 4 disclaimer text.
         if flashing_index >= len(flashing_rolling): #If the index goes over the length of the list, this will happen.
             flashing_index=0 #Flashing index is set to 0.
         flashing=flashing_rolling[int(flashing_index)] #gets the disclaimer image.
         flashing_location=flashing.get_rect(topleft=(0,0)) #Places the disclaimer image at this location.
         screen.blit(flashing, flashing_location) #Draws the disclaimer on the screen.
         mixer.music.load("Game_Files/AudioSFX/fsm-team-escp-downtown-walk.mp3") #Music loaded in, will play on the next screen.
         mixer.music.play(-1) #Loops the track.
      elif return_pressed==3: #If the enter key is pressed thrice, then this will run.
         #mixer.music.play(-1) #Loops the track.
         background_index += 0.07  # A scroll across the frames will be applied using the index.
         if background_index >= len(background_rolling): # if the index is greater than the amount of frames, then it must be reset.
            background_index = 0 #Index reset.
         background = background_rolling[int(background_index)] #The background is set to the frame chosen using the list.
         background_location = background.get_rect(topleft=(0, 0)) #background placed at this location.
         screen.blit(background, background_location) #Background is drawn.
      elif return_pressed==4: #If the enter key is pressed 4 times, then this will run.
          breakdown_index+=0.04 #Breakdown index goes up bu this number.
          if breakdown_index >= len(breakdown_rolling): # if the index is greater than the amount of frames, then it must be reset.
             breakdown_index=27 #Index set to 27.
          breakdown = breakdown_rolling[int(breakdown_index)] #The background is set to the frame chosen using the list.
          breakdown_location=breakdown.get_rect(topleft=(0,0)) 
          screen.blit(breakdown, breakdown_location) #Background is drawn.
      elif return_pressed==5: #If enter is pressed 5 times, this will run.
          bull_first_appearance_index+=0.025  # A scroll across the frames will be applied using the index.
          if bull_first_appearance_index >= len(bull_first_appearance_rolling): # if the index is greater than the amount of frames, then it must be reset.
              bull_first_appearance_index=13 #Index set to 13.
          bull_first_appearance=bull_first_appearance_rolling[int(bull_first_appearance_index)] #The background is set to the frame chosen using the list.
          bull_first_appearance_location=bull_first_appearance.get_rect(topleft=(0,0)) #background placed at this location.
          screen.blit(bull_first_appearance, bull_first_appearance_location)
      elif return_pressed==6: #If enter is pressed 6 times, this will run.
          breakdown_warning_index+=0.005 # A scroll across the frames will be applied using the index.
          if breakdown_warning_index >= len(breakdown_warning_rolling): # if the index is greater than the amount of frames, then it must be reset.
              breakdown_warning_index=0 #Index reset.
          breakdown_warning=breakdown_warning_rolling[int(breakdown_warning_index)] #The background is set to the frame chosen using the list.
          breakdown_warning_location=breakdown_warning.get_rect(topleft=(0,0)) #background placed at this location.
          screen.blit(breakdown_warning, breakdown_warning_location)#Background is drawn.
      elif return_pressed==7: #If the enter key is pressed twice, this will be drawn.
         screen.fill((255,255,255)) #Clears screen of previous screen.
         screen.blit(controls, controls_location) #The controls are displayed on the screen.
      elif return_pressed==8: #If enter pressed is 5 then this will happen.
         screen.fill((255,255,255)) #Clears screen of previous screen.
         controls=pygame.image.load('Game_Files/Assets/Stage/Controls_KBM_2.png').convert_alpha() #Screen showing the controls is loaded in.
         controls_location=controls.get_rect(topleft=(0,0)) #The location of the controls
         screen.blit(controls, controls_location) #The controls are displayed on the screen.
      elif return_pressed==9: #Otherwise, this will run.
         set_name=True #set score is set to true.
      pygame.display.update() #Screen is refreshed.

while splash_screen: #While the splash screen is true, this runs.
   if animation_active: #If the animation is active this will run.
      screen_to_take_you_to() #Nice, I figured out how to make the splash screen story work, simply by seperating the drawing logic into a function that detects how many times the enter button has been pressed.
   for event in pygame.event.get(): #The events are gathered using this for loop.
      if event.type==pygame.QUIT: #If the player presses the 'X' key, then the game will stop running.
         pygame.quit()#Pygame quits
         quit()#python quits.
      keys=pygame.key.get_pressed() #The keys are recorded
      if event.type==pygame.KEYDOWN: #If a key is pressed this will run.
         if event.key==pygame.K_ESCAPE: #If the escape key is pressed it means that the user wants to quit.
            pygame.quit() #Pygame exits.
            quit() #Python shuts down.
         if event.key==pygame.K_RETURN: #if the enter key is pressed, then return pressed will go by one which will handle which story sequence to show.
            return_pressed+=1 #Everytime enter is pressed, it will go up by one.
   if set_name: #If its time to set the user's name, then this will run.
       animation_active=False #The animation is no longer active.
       name_display = font_4.render(f"Set Name - {name_input}", True, "Green") #The user is told to set their name.
       name_display_parameters=name_display.get_rect(topleft=(0,100)) #places the name text at this location.
       name_display_2 = font_2.render("Press enter to continue", True, "Green") #When the user is done, they can proced by pressing enter.
       name_display_parameters_2=name_display_2.get_rect(topleft=(500,700)) #Places the enter text at this location.
       screen.fill((0, 0, 0))  #Fills the screen with black.
       screen.blit(name_display,  name_display_parameters) #Draws the name prompt on the screen.
       screen.blit(name_display_2, name_display_parameters_2)  #Draws the enter text on the screen.
       pygame.display.update() #Changes are updated to the screen.     
       for event in pygame.event.get(): #All events are handled, such as kbm input, mouse, etc.
            if event.type==pygame.QUIT: #If the player quits the game.
                  pygame.quit() #Pygame quits the game.
                  quit() #prevents weird issue where even if the game quit, the code still ran.
            keys=pygame.key.get_pressed() #Necessary for when multiple keys are pressed
            if event.type==pygame.KEYDOWN: #Should allow the user to see what the controls are and the objective.
                  if event.key==pygame.K_ESCAPE: #If the escape key is pressed it means that the user wants to quit.
                     pygame.quit() #Pygame exits.
                     quit() #Python shuts down.
                  if (event.unicode.isalpha() or event.unicode==' ') and len(name_input) <= 40:  #If the inputted key is in the alphabet or is a space and is smaller than or equal to 48 characters this will run.
                     name_input += event.unicode  # Adds the letter to string
                  elif event.key == pygame.K_BACKSPACE: #If the key is backspace, then a letter must be removed.
                     name_input = name_input[:-1]  # Allows deletion
                  elif event.key==pygame.K_RETURN and not name_input=="": #Takes them to the set score screen.
                     date_and_time=datetime.datetime.now()
                     set_score=True #Set score is set to true
                     set_name=False #Set name is set to false
   if set_score: #if set score is set to true, this will run.
         goal_display = font_3.render(f"Set Points Goal - MIN 100 - {goal_input}", True, "Green") #The goal being inputted is continously updated on the screen.
         goal_display_parameters=goal_display.get_rect(topleft=(0,100)) #The goal the user inputs is put into a rect.
         goal_display_2 = font_6.render("Press enter to start the game or press \"L\" to view the Scoreboard. ", True, "Green") #Prompts the user to continue the game.
         goal_display_parameters_2=goal_display_2.get_rect(topleft=(100,SCREEN_HEIGHT-100)) #Places the continue text on the screen.
         screen.fill((0, 0, 0)) #background filled with black
         screen.blit(goal_display,  goal_display_parameters)  # Positions score on the scrren.
         screen.blit(goal_display_2, goal_display_parameters_2) #Draws the text to start the game.
         pygame.display.update() #Screen is updated to show the score
         for event in pygame.event.get(): #All events are handled, such as kbm input, mouse, etc.
            if event.type==pygame.QUIT: #If the player quits the game.
                  pygame.quit() #Pygame quits the game.
                  quit() #prevents weird issue where even if the game quit, the code still ran.
            keys=pygame.key.get_pressed() #Necessary for when multiple keys are pressed
            if event.type==pygame.KEYDOWN: #Should allow the user to see what the controls are and the objective.
                  if event.key==pygame.K_ESCAPE: #If the escape key is pressed it means that the user wants to quit.
                     pygame.quit() #Pygame exits.
                     quit() #Python shuts down.
                  elif event.key==pygame.K_l: #If the user presses L, this will happen.
                      leaderboard_function() #They are taken to the leaderboard mini program.
                  elif event.unicode.isdigit() and len(goal_input) < 7:  #If the inputted key is a digit and is smaller than a million this will run.
                     goal_input += event.unicode  # Adds the digit to string
                  elif event.key == pygame.K_BACKSPACE: #If the key is backspace, then a digit must be removed.
                     goal_input = goal_input[:-1]  # Allows deletion, copilot given.
                  elif event.key==pygame.K_RETURN and (not goal_input=="" and len(goal_input) >=3): #They are ready to play the game.
                     mixer.music.stop() #Stops the track.
                     mixer.music.load("Game_Files/AudioSFX/leave.wav") #To make a dramatic entrance and stage the show.
                     mixer.music.play() #SFX plays.
                     #screen.blit(shop, shop_location) #The shop is drawn first.
                     #pygame.display.update() #Changes are updated to the screen.
                     #pygame.time.delay(3000) #Delay of 3 seconds.
                     #player_hitbox=player_jumping.get_rect(topleft=(0,0)) #Allows the player to not collide with th ebull when the game starts
                     #screen.blit(player_256, player_hitbox) #Draws the player on the screen.
                     #pygame.display.update()#Changes are updated to the screen.
                    # pygame.time.delay(3000)#Delay of 3 seconds.
                    # bull_hitbox=bull.get_rect(topleft=(1646,778)) #Places the bull at this location.
                     #screen.blit(bull, bull_hitbox) #Draws the bull on the screen.
                     #pygame.display.update()#Changes are updated to the screen.
                     #pygame.time.delay(3000)#Delay of 3 seconds.
                     goal=int(goal_input) #Converts the goal string to an int for a later comparison.
                     splash_screen=False #The spalsh screen is false.
                     set_score=False #set score is set to false
                     main_game=True #The main game can now run.
                     goal_stored=goal #The new goal stored is the goal the user inputted.
                     starting_time=pygame.time.get_ticks() #Resets the timer.
                     starting_time_secs=pygame.time.get_ticks() #Resets the seconds to start back at 0.
                     game_active=True #the game is active.
                     attempted_score=str(goal_input) #The target score is stored.
while main_game: #Handles the game loop.
  player_x=player_hitbox.left #Its accurately getting the location!
  player_y=player_hitbox.top #Same as above, to make the bull hopefully chase the player down.
  player_current_location=player_hitbox.topleft #Updates the players location continously.
 # print("Current position of player: " + str(player_current_location)) #for debugging purposes.
  for event in pygame.event.get(): #All events are handled, such as kbm input, mouse, etc.
      if event.type==pygame.QUIT: #If the player quits the game.
         pygame.quit() #Pygame quits the game.
         quit() #prevents weird issue where even if the game quit, the code still ran.
      if game_active: #If the game is active this will
         keys=pygame.key.get_pressed() #Always remember this! Also, error was that events must be handled within the event loop!
         if event.type==pygame.KEYDOWN: #If the player pushes a keydown, this will be handled.
            if event.key==pygame.K_ESCAPE: #Allows the user to quit with escape.
               pygame.quit() #Pygame quits the game.
               quit() #Quit ends the execution of the program.
            if special_speed_counter > 0: #Had to be seperated to prevent issue where the dashes got reduced by two due to interference between key pressed (which runs every frame) and keydown which would only run once when the key is initially pressed.
                  if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]): #This is where get pressed comes into play, because event key can only...
                     #register one event at a time.
                     player_speed = -30 #Player moves way faster than the bull to the left.
                     special_speed_counter=special_speed_counter-1 #One of the special dashes is removed from the user.
                     special=font_4.render("Dashes remaining: " + str(special_speed_counter), True, 'Black')  #Dashes remaining is rerendered.
                     special_location=special.get_rect(topleft=(475,0)) #Dashes are drawn at this location.
                  elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and special_speed_counter > 0: #Same as above but for right movement.
                     special_speed_counter=special_speed_counter-1 #One of the special dashes is removed from the user.
                     player_speed = +30 #Player moves way faster than the bull to the right.
                     special=font_4.render("Dashes remaining: " + str(special_speed_counter), True, 'Black') #Dashes remaining is rerendered.
                     special_location=special.get_rect(topleft=(475,0)) #Dashes are drawn at this location.
            if event.key==pygame.K_w or event.key==pygame.K_SPACE or event.key==pygame.K_UP: #If the key pressed is w or space or up, this happens.
               player_gravity = -26 #Player gravity is set to -26, which is tied to the y movement.
            if event.key==pygame.K_s or event.key==pygame.K_DOWN: #If the s or down is pressed this will run.
               player_gravity = +33 #Player gravity is set to 30, which is  also tied to the y movement.
            if event.key==pygame.K_a or event.key==pygame.K_LEFT: #If the key pressed is a or left this will happen.
               player_speed= -10 #player speed is set to -10, which is tied to the x axis.
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT: #If the user presses d or right this will run.
               player_speed= 10 #player speed is set to 10, which is tied to the x axis.
         if event.type == pygame.KEYUP: #Deals with horizontal movement across the x axis from L to R.
            if event.key==pygame.K_a or event.key==pygame.K_LEFT: #If the player presses a or left, this will run.
               player_speed=0 #Player speed set to 0 to stop movement.
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT: #If the user lets of the d or right key this will run.
               player_speed=0 #Player speed set to 0 to stop movement.
      elif (not game_active and not game_over): #If the game is not active, and it is not a game over this will run.
         special_speed_counter=3  #Special dashes is reset to 3.
         goal_display = font_2.render(f"Set A New Points Goal - MIN 100 - {goal_input}", True, "Green") #The goal being inputted is continously updated on the screen.
         goal_display_parameters=goal_display.get_rect(topleft=(0,0)) #The goal the user inputs is put into a rect.
         goal_display_2 = font_6.render("Press enter to start the game or press \"L\" to view the Scoreboard. ", True, "Green") #Prompts the user to continue the game.
         goal_display_parameters_2=goal_display_2.get_rect(topleft=(75,1000)) #Tells the user their options 
         previous_score=font_2.render(f"Previous - {goal_stored}", True, "Green") #The previous score the user attempted is displayed on the screen.
         previous_score_parameters=previous_score.get_rect(topleft=(0, 100)) #Puts the previous score on the bottom of the set score screen.
         screen.fill((0, 0, 0)) #background filled with black
         screen.blit(goal_display,  goal_display_parameters)  # Positions score on the scrren.
         screen.blit(goal_display_2, goal_display_parameters_2) #Draws prompt
         screen.blit(previous_score, previous_score_parameters) #Shows the previous score to the user.
         pygame.display.update() #Screen is updated to show the score
         keys=pygame.key.get_pressed() #Always remember this! Also, error was that events must be handled within the event loop!
         if event.type==pygame.KEYDOWN: #If a button is pressed, this will be checked.
            if event.key==pygame.K_ESCAPE: #Allows the user to quit with escape.
               pygame.quit() #Pygame quits the game.
               quit() #Quit ends the execution of the program.
            elif event.key==pygame.K_l: #If the user inputs L, this will happen.
                leaderboard_function() #They are taken to the leaderboard mini program.
            elif event.unicode.isdigit() and len(goal_input) < 7:  #If the inputted key is a digit and is smaller than a million this will run.
               goal_input += event.unicode  # Adds the digit to string
            elif event.key == pygame.K_BACKSPACE: #If the key is backspace, then a digit must be removed.
               goal_input = goal_input[:-1]  # Allows deletion, copilot given.
            elif event.key==pygame.K_RETURN and (not goal_input=="" and len(goal_input) >=3): #They are ready to play the game.
               score=0 #Score is set to 0 
               player_hitbox.y=starting_pos #Allows the player to not collide with th ebull when the game starts
               player_speed=0 #Prevents left over horizontal movement.
               points_text=font_2.render("Points: 0 ", True, "Black") #Points are reset to 0.
               points_text_box=points_text.get_rect(topleft=(0,0)) #Points drawn at this location.
               player_hitbox.x=(SCREEN_WIDTH / 2) #The player is placed at the specified location.
               bull_hitbox=bull.get_rect(midbottom=(SCREEN_WIDTH / 2 + SCREEN_WIDTH / 3, SCREEN_HEIGHT - 75)) #Bull is placed at specific location on the screen.
               bull_last_seen = pygame.time.get_ticks() #When the bull was last seen is reset
               bull_movement_cooldown = random.randint(1000, 2000) #The cooldwon is reset.
               bull_speed = 0 #The bulls speed is set to 0
               bull_gravity = 0 #The bulls gravity is set to 0
               inner_loop_x = False # Innerr_loop_x is set to false.
               goal=int(goal_input) #Converts the goal string to an int for a later comparison.
               game_active=True #Game active is set to true.
               goal_stored=goal #goal stored is the new input.
               starting_time=pygame.time.get_ticks() #Resets the timer.
               starting_time_secs=pygame.time.get_ticks() #Resets the seconds to start back at 0.
               time_keep=True #The timer can be used.
               projectile_last_seen=pygame.time.get_ticks() #Projectile timer for last seen is set when the game starts.
               warning_active=False #The warning is not active to prevent carryover from the previous session.
               projectile_active=False #The projectile is also not active for the same reason.
               warning_x=0 #Warning x is set to 0 because the projectile will always be from left to right.
               warning_y=random.randint(0, 450) #A random y for the warning is chosen.
               projectile_x=warning_x #Projectile x is set to the value of warning x.
               projectile_y=warning_y #Projectile y is set to the value of warning y.
               projectile_location=projectile.get_rect(topleft=(projectile_x, projectile_y)) #Sets the projectile at this location.
               warning_checked=0 #Warning checked is set to 0.
               special_speed_counter=3 #Player gets 3 dashes.
               special=font_4.render("Dashes remaining: " + str(special_speed_counter), True, 'Black') #Tells the user how many dashes they have.
               special_location=special.get_rect(topleft=(475,0)) #Dashes drawn at this location.
      else: #This took an extremely long time to figure out, but I cracked it after two days.
               success=False #Success is set to false.
               #Literally, just draw the game over screen here instead of using a function and if the user presses enter then set the game_over flag to false which
               #would trigger the above code to run.
               #Seriously, it was that easy, I'm glad I was able to figure out through trial and error.
               #since it used to be a local variable, so now it works.
               score_game_over=str(score) #I was able to Fix the issue where score was going up on key up, I had to basically like just make the score be at outside of the main loop
               score_game_over_text=font_2.render(score_game_over, True, "Red") # The score of the last attempt will be drawn using this.
               score_game_over_text_rect=score_game_over_text.get_rect(topleft=(130,200)) #Last atttempt score will be drawn at this location.
               total_time_text=font_2.render(total_time, True, "Red") #The final time is shown on the screen.
               total_time_text_rect=total_time_text.get_rect(topleft=(1375,200)) #Sets the location of the final time.
               screen.blit(game_over_screen, game_over_draw) #Game over screen is drawn.
               screen.blit(score_game_over_text, score_game_over_text_rect) #The players last score is drawn to the screen.
               screen.blit(total_time_text, total_time_text_rect) #Shows the final time on the screen.
               pygame.display.update() #Screen is refreshed.
               if event.type==pygame.KEYDOWN: #If a button is pressed, this will be checked.
                  if event.key==pygame.K_ESCAPE: #Allows the user to quit with escape.
                     pygame.quit() #Pygame quits the game.
                     quit() #Quit ends the execution of the program.
                  if event.key == pygame.K_RETURN: #The player is taken to the screen to enter the goal.
                     points=0 #Fixed issue with points not becoming 0 again.
                     game_over=False #Game over is no longer false
                     mixer.music.stop() #Stops the music from playing.

  if game_active: #If the game is active this will run.
     print("Bull is at: x " + str(bull_hitbox.x) + " y: " + str(bull_hitbox.y)) #Debug
     time_keep=True #The timer is true.
     def points_system(): #This function handles how points will be distributed.
        global points #Without this, cannot reach points and update variable accordingly.
        item_hitbox.y=10000 #Since assets cannot despwan, it is instead moved out of sight from the player.
        print("They have collided!") #Debuggin tool
        points+=10 #10 points are added to the users score.
        print(points) #points are printed in the console to debug.
        return str(points) #Points MUST be returned as str because Python will not accept an integer for the text font.
     def bull_lock_on(): #A function call bull_lock_on handles thee charging of the bull
         global bull_speed #the bull speed is now modified using the global keyword.
         global bull_gravity #the bull gravity is now modified using the global keyword.
         global bull_movement_cooldown #the bull movement cooldown is now modified using the global keyword.
         global bull_last_seen #When the bull is last seen, is modified using the global keyword.
         global inner_loop_x #This is why movement wasn't happening, because I had failed to modify the inner_loop!
         global inner_loop_y #inner loop y is now accesible
         global bull_charging #bull charging flag is now accesible
         bull_dice_roll=random.randint(0,5) #Chooses between 0 and 1 to avoid weird movement that caused the bull to move in a circle.
         if bull_dice_roll < 4: #If the bull dice roll is less than 4, this will run. Reworked to force the bull to chase the player more.
            inner_loop_x=True #The inner loop for x movement is set to true.
            bull_last_seen=pygame.time.get_ticks() #Bull last seen updates its time to what it is now.
            bull_movement_cooldown=random.randint(1000,2000) #A cooldown of between 1 and 2 seconds is made.
         else: #Otherwise, this happens
            inner_loop_y=True #inner loop y is set to true, which allows the bull to chase the player up and down.
            bull_charging=True #Bull charging is set to true. Which prevents janky movement.
            bull_last_seen=pygame.time.get_ticks() #Bull last seen updates its time to what it is now.
            bull_movement_cooldown=random.randint(1000,2000) #A cooldown of between 1 and 2 seconds is made.
     #if bull_hitbox.x >=1675: #If the bull attempts to go off the screen, this will happen.
        #bull_speed=0 #Bull speed is set to 0.
        #bull_hitbox.x=1674 #The bull is placed back within the dimensions. Scrapped as it made it too easy for the player to camp, practicaility > looks.
     if player_hitbox.y <= 0: #If the player tries to go out of bounds for the y axis this happens.
        player_gravity=0 #Player gravity is set to 0.
     if player_hitbox.x <= 0: # If the player attempts to move outside of the screen's left x axis, this happens.
        player_speed=0 #Player speed is set to 0;.
        player_hitbox.x=1 #Puts the player back on the screen.
     if player_hitbox.x >= 1850: # If the player attempts to move outside of the screen's right x axis, this happens.
        player_speed=0 #Player speed is set to 0;.
        player_hitbox.x=1849 #Player is put at this x location.
     if player_hitbox.colliderect(item_hitbox): #If the player and the item collide, these statements will run.
        score=points_system() #Score variable is a ssigned to the points returned
        points_text=font_2.render("Points " + score, True, "Black") #A rect object that contains the updated score is made.
        points_text_box=points_text.get_rect(topleft=(0, 0)) #Sets the points location on the screen.
        if int(score) >= goal: #A score to win will be determined. For now, it is set to 10.
           mixer.music.load("Game_Files/AudioSFX/crowd-cheer.wav") #A cheering sound is played when the user succeeds
           mixer.music.play() #The cheer is played
           success=True #Success is set to true.
           with open ("Scoreboard.txt", "a") as f: #Stores the users name,time and score to a file.
                     f.write("\n\nName- " + name_input.upper() + "\nDate - " + date_and_time.strftime("%x") + "\nObtained Minimum Score-" + str(goal) + "\nFinal Score- " + str(score) + "\nFinal Time: " + total_time_2 + "\nRESULT: MISSION SUCCESS!")     
           print(total_time) #For debugging purposes.
           game_active=False #The game is paused
           points=0 #Points are reset
           goal_input='' #Goal input is blank for now.
           fake_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_e, 'unicode': '\r'}) #Needed because the screen would not refresh to the input screen,
           #regardless of where the rendering logic was. At first glance, it seemed like it could be because of the event handler,
           #but moving the logic of the code that drew to the screen outside of that also rendered no results. It is also not abundantly clear what could be causing this,
           #since multiple checks and modifications do not see a key conflict or a required key press, hence this fake event.
           pygame.event.post(fake_event) #Tells the event handler that this key was pressed
     current_time=pygame.time.get_ticks() #The current time in milliseconds is obtained.
     player_gravity += 1  #Player gravity increases by 1 every time to make the player go down after the have moved up in the air
     player_hitbox.y += player_gravity #The player will now move down the y axis thanks to the gravity preset.
     if player_hitbox.bottom >= starting_pos: #If the players is higher than the starting position than they must have the ground limit to prevent clipping on the way down.
        player_hitbox.bottom = starting_pos #Sets the ground to where the player started
        player_gravity = 0 # Resets the gravity to prevent the player from clipping.
     if bull_hitbox.bottom >= bull_starting_pos:#If the bull  is higher than the starting position than the bull must have the ground limit to prevent clipping on the way down.
        bull_hitbox.bottom = bull_starting_pos #Sets the ground to where the bull started
        bull_gravity= 0 # Resets the gravity to prevent the bull from clipping.
     player_hitbox.x+=player_speed #The player will move alongside the x axis left to right according to the player speed.
     screen.fill((0, 0, 0)) #Screen is filled with black to prevent trailing effect.
     screen.blit(shop, shop_location) #Draws the shop before anything else.
     screen.blit(player_256, player_hitbox) #Player drawn onto the screen.
     screen.blit(bull, bull_hitbox) #The bull is drawn on the screen.
     if current_time - item_last_seen >= item_respawn_cooldown: #If the time elapsed is greater than the cooldown this will run.
        while True: #This loop will continously generate x and y value  for the item until there is no overlap with the bull.
               item_x_pos=random.randint(200,1581) #Remember, you need to subtract the width and the height of the object to prevent it from going off the screen
               item_y_pos=random.randint(500,600) #Remember, you need to subtract the width and the height of the object to prevent it from going off the screen
               item_hitbox.topleft = (item_x_pos, item_y_pos) #The item will be drawn at this location.
               if item_hitbox.right < bull_hitbox.left: #If the item is to the left of the bull this will be allowed.
                  print("item is to the left of the bull") #For debug purposes.
                  print("Bull left: " + str(bull_hitbox.left) + " and item right: " + str(item_hitbox.right)) #Debugging tool.
                  item_last_seen = current_time #Item last seen is set to the current time.
                  item_respawn_cooldown = random.randint(2000, 5000) #The cooldown is restarted.
                  break #Loop is broken.
               elif item_hitbox.left > bull_hitbox.right:  #If the item is to the right of the bull this will be allowed.
                  print("item is to the right of the bull")  #Debug 
                  print("Bull right: " + str(bull_hitbox.right) +  " item left: " + str(item_hitbox.left)) #Debug
                  item_last_seen = current_time #The item last seen timer is set to the current time.
                  item_respawn_cooldown = random.randint(2000, 5000) #The cooldown is restarted.
                  break #Loop breaks.
               else: #Otherwise, the loop must continue.
                  #Debug tool.
                  print("Not good to spawn here. Bull left: " + str(bull_hitbox.left) + " and item left: " + str(item_hitbox.left) + "/n Bull right: " + str(bull_hitbox.right) +  " item right: " + str(item_hitbox.right))
     if current_time - water_puddle_last_seen >= water_puddle_cooldown: #if the water cooldown period is exceeded this will run.
        water_possible_locations=[0, 393] #Allows a better way to put the water hazrd on screen.
        water_location_select=random.choice(water_possible_locations) #Chooses a random place to place the water puddle across the x axis.
        water_puddle_last_seen=current_time #The water puddle hazard would last be seen at that time.
        water_puddle_x=water_location_select#Water puddle_x is tthen set to be at this location. Default 100 to SCREEB_WIDTH  - 350 #REWORKED FOR BETTER LOGIC
        water_puddle_y=starting_pos - 110 #Water puddle y location is set.
        water_puddle_location.topleft=(water_puddle_x, water_puddle_y) #Water puddle is drawn at this location.
        water_possible_locations_2=[785, SCREEN_WIDTH-350] #The water puddle facing right can be at these locations.
        water_location_select_2=random.choice(water_possible_locations_2) #A random choice is made to select the location to draw the water.
        water_puddle_x_2=water_location_select_2 #The water puddles x location is the one that was randomly chosen.
        water_puddle_y_2=starting_pos-110 #Water puddle's y location is set here.
        water_puddle_location_2.topleft=(water_puddle_x_2, water_puddle_y_2) #The water puddle will be drawn at this location.
        print(water_puddle_x) #For debug purposes.
        water_puddle_cooldown=random.randint(5000,10000) #Water puddle cooldown is reset.
     if not bull_charging and current_time - bull_last_seen >= bull_movement_cooldown: #If the bull has not moved in a certain amount of time and the bull is not currently charging this will run.
        bull_lock_on() #Calls the bull lock on function.
     if inner_loop_x: #If the inner loop is true, this will run.
        if bull_hitbox.right < player_hitbox.left: #If the bull is in a position left of the player, it must move right.
           bull=pygame.image.load("Game_Files/Assets/Bull/bull_256.png")
           bull_speed=17 #Bull speed is set to 17.
           bull_hitbox.x += bull_speed  # Moves the bull to the right of the screen.
        elif bull_hitbox.left > player_hitbox.right: #If the bull is to the right of the player, it must move to the left.
             bull=pygame.image.load("Game_Files/Assets/Bull/bull_256_left.png")
             #bull_hitbox=bull.get_rect(topleft())
             bull_speed=17 #Bull speed is set to 17.
             bull_hitbox.x -= bull_speed # Moves the bull to the left of the player.
        else: #Otherwise, if the bull is neither to the left or right of the player, then it is assumed that the bull and the player are the same x location.
              inner_loop_x = False  #Bull does not need to move, so inner_loop boolean is set to false.
              inner_loop_y = True #The inner loop y is set to true to make the bull follow the player across the y axis
     if inner_loop_y: #If the inner loop is true, this will run.
        if bull_hitbox.bottom < player_hitbox.top :#If the bull is higher than the player, then it must be brought down.
             bull_hitbox.y += 25 # Moves the bull to the bottom of the screen 25 is default
        elif bull_hitbox.top > player_hitbox.bottom: #If the bull is to the bottom of the player, it must move up.
             bull_hitbox.y -= 33 # Moves the bull to the top of the screen.
        else: #Otherwise, if the bull is neither to the left or right of the player, then it is assumed that the bull and the player are the same y location.
              inner_loop_y = False  #Bull does not need to move, so inner_loop boolean is set to false.
              bull_charging=False #Bull charging is set to false, which means the cooldown can work properly now.
     if bull_hitbox.colliderect(item_hitbox) and points >= 20: #if the bull collides with the item, this will happen.
        item_hitbox.y=10000 # The item will move out the way
        points-=20 #The points get reduced by 20.
        #points_text=font_5.render(f"Bull Got Item...-20 POINTS!", True, "RED") #Removes the points and displays on screen
        points_text=font_2.render("Points - " + str(points), True, "Red") #A rect object that contains the updated score is made.
        points_text_box=points_text.get_rect(topleft=(0, 0)) #Sets the points location on the screen.
        print("The bull got this item!") #For debug purposes.
     if bull_hitbox.colliderect(player_hitbox): # If the bull touches the player this will happen.
        score_game_over=str(score) #I was able to Fix the issue where score was going up on key up, I had to basically like just make the score be at outside of the main loop
        with open ("Scoreboard.txt", "a") as f: #Appends the failed game text to the file.
                     f.write("\n\nName- " + name_input.upper() + "\nDate - " + date_and_time.strftime("%x") + "\nTarget Score-" + str(goal) + "\nLast Attempt Score- " + score_game_over + "\n" + "\nRESULT: NOT SUCCESSFUL")     
        time_keep=False #Tells the program to not keep taking the time.
        print(total_time) #For debug
        mixer.music.load("Game_Files/AudioSFX/aylex-tension-rising.mp3") #Track attribution within files. Has to be done here because otherwise the music 
        #would glitch out for an event due to the event handler.
        mixer.music.play(-1) #Plays the music loaded in.
        game_active=False #Game active is false
        game_over=True #Game over is set to true
        fake_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_e, 'unicode': '\r'}) #Like above, this is needed because the game over screen wouldnt show without input
        #so i used the same method I discovered before again and it works properly.
        pygame.event.post(fake_event) #Tells the event handler that this key was pressed
     if player_hitbox.colliderect(water_puddle_location): #If the player collides with the water hazard, then they must be slowed down. They can stil jump normally as gravity is not affected here.
        keys=pygame.key.get_pressed() #Keys needed because otherwise it cannot detect it, I believe it is due to the event handler interfering.
        if (keys[pygame.K_a]) or (keys[pygame.K_LEFT]): #If left or a is pressed, then the player speed will be adjusted in this way.
           player_speed=-5 #Player speed is reduced.
           print("Water hazard, moving left.") #Debug purposes.
        elif (keys[pygame.K_d]) or (keys[pygame.K_RIGHT]): #If right or d is pressed, then the player speed will be adjusted in this way.
           player_speed=5 #Player speed is reduced.
           print("Water hazard, moving right.") #Debug purposes.
     if player_hitbox.colliderect(water_puddle_location_2): #If the player collides with the water hazard, then they must be slowed down. They can stil jump normally as gravity is not affected here.
        keys=pygame.key.get_pressed() #Keys needed because otherwise it cannot detect it, I believe it is due to the event handler interfering.
        if (keys[pygame.K_a]) or (keys[pygame.K_LEFT]): #If left or a is pressed, then the player speed will be adjusted in this way.
           player_speed=-5 #Player speed is reduced.
           print("Water hazard, moving left.") #Debug purposes.
        elif (keys[pygame.K_d]) or (keys[pygame.K_RIGHT]): #If right or d is pressed, then the player speed will be adjusted in this way.
           player_speed=5 #Player speed is reduced.
           print("Water hazard, moving right.") #Debug purposes.
     time_message=font_2.render("Stopwatch in Minutes", 'True', 'Black') #Stopwwatch messaged rendered.
     time_message_textbox=time_message.get_rect(topleft=(1160,0)) #Stopwtach messaged placed at this location.
     if time_keep: #as long as the timer is set to ne true, this will run.
        seconds=int((pygame.time.get_ticks() - starting_time_secs)/1000) #The seconds are stored seperately to allow a reset of the seconds, but not the minutes.
        if seconds >= 60:#To prevent the seconds from ticking up again.
           starting_time_secs=pygame.time.get_ticks() #Resets the seconds to start back at 0.
           special_speed_counter+=1 #The player gets one dash added for every minute they survive
           special=font_4.render("Dashes remaining: " + str(special_speed_counter), True, 'Black') #the new amount of dashes is placed on the screen.
           special_location=special.get_rect(topleft=(475,0)) #New dashes placed at this location.
        current_time_disp=font_2.render("MIN " + str(int((pygame.time.get_ticks() - starting_time)/60000)) + "                         SEC " + str(seconds), 'True', 'Black') #The clock is shown on the screen, wrapped in multiple braces to avoid weird clock issues.
        total_time=str(int((pygame.time.get_ticks() - starting_time)/60000)) + " M " + str(seconds) + " S" #The total time is stored, which is useful for the game over and mission accomplished screens.
        total_time_2=str(int((pygame.time.get_ticks() - starting_time)/60000)) + " Minutes and " + str(seconds) + " Seconds. " #Meant to be used for the file saving feature.
        current_time_textbox=current_time_disp.get_rect(topleft=(1160,60)) #places the timer on the specific location on screen.
        screen.blit(current_time_disp, current_time_textbox) #The time is shown on the screen.
     if current_time - projectile_last_seen > projectile_cooldown: #FINALLY, AFTER A WHOLE 3 DAYS, THIS WORKS! Timer used to determined if projectile ready to be shown.
        warning_location=warning.get_rect(topleft=(warning_x, warning_y)) # A warning is ready to be shown at this location.
        #The issue was that warning x was getting reassigned even wit the projectile active boolean set to false.
        #This caused the projectile to be drawn on the screen twice incorrectly.
        warning_active=True #Flag that the warning is active is set to true.
     if warning_active: #If the warning is active this will run.
        screen.blit(warning, warning_location) #Warning drawn on this location on the screen.
        warning_checked+=1 #Warning checked gets 1 added, this allows the time to be checked precisely ONCE!
        if warning_checked > 0 and warning_checked < 2: #Provided warning checked is greater than 0 and less than two, this will run.
           print("Comparison reached") #Prints that the comparison was reached
           warning_last_seen=pygame.time.get_ticks() #Time checked precisely once rather than having to reset it.
           warning_x=0 #Warning_x is also set to 0 precisely once, which prevents an issue whre the x would constantly be set to 0
           #which prevented the comparison later to not work.
           print(str(warning_last_seen) + " was last seen at this time.") #For debug purposes.
        if current_time - warning_last_seen > warn_window: #If the warning has passed 5 seconds, the projectile can now be shown.
            projectile_active=True #Projectile active is now set to true.
            print("projectile can now be shown.")
     if projectile_active: #If the projectile_active is true, this can run.
        warning_active=False #The warning is no loner active
        projectile_x+=35 #Projectile will move across the x axis at this rate.
        if projectile_x <= 1920: #If the proectile is not off the screen, this can run.
            projectile_location=projectile.get_rect(topleft=(projectile_x, projectile_y)) #Projectile is placed at this location.
            screen.blit(projectile, projectile_location) #Projectile drawn at this location.
            if player_hitbox.colliderect(projectile_location): #If the player collides with the projectile this will happen.
                  projectile_x=2000 #Projectile is moved off the screen.
                  player_hitbox.y+=SCREEN_WIDTH #Will stun the player to where they immediately fall to the ground.
                  if points >= 50: #If the player has more than 50 points, then this will run.
                     points-=50 #50 points are deducted from the player
                     points_text=font_2.render("Points " + str(points), True, "RED") #A rect object that contains the updated score is made.
                     points_text_box=points_text.get_rect(topleft=(0, 0)) #Sets the points location on the screen.
                  else: #Otherwise, its over.
                     mixer.music.load("Game_Files/AudioSFX/aylex-tension-rising.mp3") #Track attribution within files. Has to be done here because otherwise the music 
                     mixer.music.play(-1) #Plays the music loaded in.
                     game_active=False #The game is no longer active.
                     game_over=True #game over is set to true.
                     fake_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_e, 'unicode': '\r'}) #fake event is made.
                     pygame.event.post(fake_event) #Tells the event handler that this key was pressed
        else: #If the projectile is off the screen this will run.
            projectile_active=False #Projectile active is set to false.
            print("The projectle is now deactived.") #For debug
            projectile_last_seen=current_time #Projectile last seen is set to current time.
            warning_y=random.randint(0, 450) #The warning's y location is set to a random location, this also serves as the y location for the projectile.
            projectile_x=warning_x #Projectile x location is set to the warning's x location.
            projectile_y=warning_y #Projectile's y location is set to the warning's y location.
            projectile_cooldown=random.randint(5000,7000) #The cooldown is reset.
            warning_checked=0 #Warning checked is equal to 0.
     bull_gravity+=1 #Brings the bull back to the ground.
     bull_hitbox.y+=bull_gravity #Bull moves accordingly to the increasing gravity.
     player_sprites() #Sprites for player function called.
     screen.blit(item, item_hitbox) #item is drawn on the screen.
     screen.blit(water_puddle, water_puddle_location) #The water puddle facing left is drawn on screen.
     screen.blit(water_puddle_2, water_puddle_location_2) #The water puddle facing right is drawn on screen.
     screen.blit(points_text, points_text_box) #points are displayed on the screen.
     screen.blit(time_message, time_message_textbox) #The timer is displayed on screen.
     screen.blit(special, special_location) #The dashes are drawn on screen.
     pygame.display.update() #Screen is refreshed
     clock.tick(60) #Frame rate is set to a max of 60.
   



