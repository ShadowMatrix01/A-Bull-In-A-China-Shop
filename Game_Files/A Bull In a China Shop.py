#Author: Jhan Gomez <br>
#Date: 07-01-2025, 8:15 PM EST  <br>
#Version (Pre-Release): 1.0.6 <br>
#Purpose: To make a fun game in PyGame that also demonstrates my understanding of python such as libraries, loops, conditionals, branching, front-end graphics, back-end code, and more.  <br>
#DONE: Controls screen, Bull movement across the x axis, bull drawing, item spawning and respawning logic, points accumulated, player when stationary, player when jumping, windows scaling set to 100%, bgm (select), out of bounds, warn and projectile system. <br>
#Fully complete bull and item logic.
#To-Draw: store, item, the three phases, and environmental hazards, item spawn, story, ground, splash screen, player when moving. <br>
#To-Do and IDEAS:  <br>
#Every 20 seconds, a third of the shop gets destroyed, which is why you must get all of the item before the time runs out  <br>
#HAZARD: Maybe, if you aren't careful, and say you get accidentally covered by red cape, he charges towards you for 3 seconds!  <br>
#If the bull collides with the item, he takes it, and you have 3 seconds to get it back from him, which you can do by jumping on him!  <br>
#If they run out of time and do not get the item back safely, 6 seconds per 1 item, they get a game over screen showing their final score.  <br>
#After everything is done, consider adding hazards such as falling debris, pool of water across the x axis (if you collide with it you move slower and so does the bull!), paint, etc  <br>
#Animation for background needed!  <br>
# Laid ground work for game_over screen.  <br>
# Fixed item spawning to not go off screen.
# Fixed transparency on image, had to change starting y position
# HAZARD: WATER PIPES ON THE BOTTOM WILL SHOOT OUT WATER PROJECTILES FROM BOTTOM TO TOP, IF THE PLAYER TOUCHES IT, THE WILL GET 1 LIFE REDUCED (TOTAL 3). Gravity from bottom to top, and drawing said pipes.
# [TOOL] A freeze in place, freezes everything except for the player and the item, but only for 3 seconds. Make sound play when pipe is about to blast out water

# DIFFERENT NOW: INSTEAD OF COUNTDOWW, TIMER COUNTS UP SO THE GOAL IS TO BEAT YOUR OWN RECORD!
#Save high score + time and name to file.


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
import random #Random module imported in.
pygame.init() #Pygame is initialized.
SCREEN_WIDTH=1920 #Screen width is set to be 1920
SCREEN_HEIGHT=1080 #Screen height is set to be 1080.
return_pressed=0
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #The dimensions are now set to be the displays dimensions.
game_active=True #This boolean allows pausing for when the player either wins or looses.
clock=pygame.time.Clock() #Allows a consistent frame rate in my game.
font=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 100) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
font_2=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 50) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
font_3=pygame.font.Font('Game_Files/Font/Arcade_Font.ttf', 75) #Karmatic Arcade font used courtesy of Vic Feiger, https://www.dafont.com/karmatic-arcade.font?l[]=10&l[]=1
starting_time=pygame.time.get_ticks() #Used for the timer.
starting_time_secs=pygame.time.get_ticks() #Used for the timer in seconds.
#Sprites for animationms
controls=pygame.image.load('Game_Files/Assets/Controls_KBM.png').convert_alpha() #Screen showing the controls is loaded in.
controls_location=controls.get_rect(topleft=(0,0)) #The location of the controls
player_walking_1=pygame.image.load('Game_Files/Assets/player_stationary.png').convert_alpha() #Asset loaded in, convert alpha helps it have the higest quality.
player_walking_2=pygame.image.load('Game_Files/Assets/player_stationary.png').convert_alpha() #Asset loaded in, convert alpha helps it have the higest quality.
player_walking=[player_walking_1, player_walking_2] #Has two sprites, can be changed.
player_walking_index=0 #Allows one of the above indexes to be selected to animate
player_256=player_walking[player_walking_index] #The sprite chosen is the one at the specified index position within the array.
player_hitbox = player_256.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 75)) #Works regardless of screen size chosen.
player_jumping=pygame.image.load('Game_Files/Assets/player_jumping.png').convert_alpha() #Jumping animation for player.

#Add special loot, cooldown, current time, add final time to game over screen, mechanics at a glance.
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
game_over_screen=pygame.image.load('Game_Files/Assets/Game_Over.png').convert_alpha() #Game over screen loaded in when drawn.
game_over_draw=game_over_screen.get_rect(topleft=(0, 0)) #Location of game over screen declared.

#Assets and Locations
item=pygame.image.load('Game_Files/Assets/Necklace.png').convert_alpha() #Necklace asset loaded in.
goal=0 #Goal is set to be a default of 0
goal_input = "" #Gets the users desired score
player_speed=0 #Default player speed is set to 0.
player_gravity=0 #Player gravity is set to 0.
special_speed_counter=3 #Allows the player to use a special dash for a total of 3 times.
starting_pos=player_hitbox.y #The starting pos of the player is set to the initial y location of the player.
player_x=player_hitbox.left #To make the bull chase the player down.
player_y=player_hitbox.top #Same as above, to make the bull hopefully chase the player down.
player_current_location=player_hitbox.topleft #top and left are combined to get an accurate x and y location for the player.
item_last_seen=pygame.time.get_ticks() #Stores the last time the item was seen.
item_respawn_cooldown=random.randint(2000,5000) #A cooldown of between 3 and 5 seconds is made.
item_x_pos=random.randint(300,1581) #Default x value range for normal items
item_y_pos=random.randint(300,550) #Default y valur range for normal items.
item_hitbox=item.get_rect(topleft=(item_x_pos, item_y_pos)) #The item is placed at the randomly generated x and y positions.
points=0 #Points counter, default is 0.
points_text=font_2.render("Points: 0 ", True, "White") #At the beggining, the score is 0 and that is displayed on the screen.
points_text_box=points_text.get_rect(topleft=(0, 0)) #Sets the points location on the screen.
bull=pygame.image.load('Game_Files/Assets/bull_256.png') #Loads the bull asset. Imagee will change depending on whether the bull is moving left or right.
bull_hitbox=bull.get_rect(midbottom=(SCREEN_WIDTH-129, SCREEN_HEIGHT-75)) #Bull is placed at specific location on the screen.
bull_starting_pos=bull_hitbox.y #Bull's starting position is stored for later gravitational calculations.
bull_x=bull_hitbox.left #The bull x location is set to be wherever the bulls left rect position is.
bull_y=bull_hitbox.top #The bull's y lpcation is set ot be wherever the top of the rect is.
bull_current_location=bull_hitbox.topleft #Top and left are combined to get the bulls current location.
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
total_time=""
#Water puddle hazard and drawing on screen.
water_puddle=pygame.image.load('Game_Files/Assets/water-test.png').convert_alpha() #Picture loaded in as water_puddle
water_puddle_2=pygame.image.load('Game_Files/Assets/water-test-2.png').convert_alpha()
water_possible_locations=[0, 393] #Possible locations for the water puddle.
water_possible_locations_2=[785, SCREEN_WIDTH-350] #Possible locations for the water puddle.
water_location_select=random.choice(water_possible_locations) #Selects a location to choose from for the water.
water_location_select_2=random.choice(water_possible_locations_2)
water_puddle_x=water_location_select #Water puddle can appear at these locations at the x axis 
water_puddle_y=starting_pos - 100 #Water puddle y is always set to this locations
water_puddle_location=water_puddle.get_rect(topleft=(water_puddle_x, water_puddle_y)) #The water hazard is drawn at this location.
water_puddle_x_2=water_location_select_2 #Water puddle can appear at these locations at the x axis 
water_puddle_y_2=starting_pos - 100 #Water puddle y is always set to this locations
water_puddle_location_2=water_puddle.get_rect(topleft=(water_puddle_x_2, water_puddle_y_2)) #The water hazard is drawn at this location.
water_puddle_cooldown=random.randint(5000,10000) #The water hazard will be redrawn every 5 to 10 seconds.
water_puddle_last_seen=pygame.time.get_ticks() #Will check when the water puddle was last seen.
score=0 #Score is by default set to 0.
set_score=False #This flag determines whether or not the user can input the score
time_keep=True #this flag determines whether the timer is active, useful for when game over or mission accomplished.
mixer.init() #Needed for music and sfx later on.
#projectile=pygame.image.load("Game_Files/Assets/Danger.png").convert_alpha()
#warning=pygame.image.load("Game_Files/Assets/Warning.png").convert_alpha()
warning_active=False # A flag used to see if the warning is active is made.
warn_window=5000 #The user will get 5 seconds to react to the projectile
warning_x=0 #Warning x is initally set to 0.
warning_y=0 #Warning y is initially set to 0.
projectile_x=warning_x #projectile x is set to warning x.
projectile_y=warning_y #Projectile y is set to warning y.
#projectile_location=projectile.get_rect(topleft=(projectile_x, projectile_y))
#warning_location=warning.get_rect(topleft=(warning_x, warning_y))
projectile_active=False #This flag is used to see if the projectile should be launched.
projectile_last_seen=pygame.time.get_ticks() #A timer is used to see when the projectile was last seen.
projectile_cooldown=random.randint(5000,10000) #A cooldown determines how much time should pass before the projectile is shown on the screen.
warning_last_seen=pygame.time.get_ticks() #used to see when the warning was last seen.
warning_checked=0 #Warning checked is used to check the time once, against the warn window.
#Reworked, allows for story to be drawn in.
while splash_screen: #While the splash screen is true, this runs.
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
            screen_to_take_you_to() #Nice, I figured out how to make the splash screen story work, simply by seperating the drawing logic into a function that detects how many times the enter button has been pressed.
   
   def screen_to_take_you_to(): #A function handles which screen is drawn.
      global set_score #set score is set at the global level.
      if return_pressed==1: #If the enter key is pressed once, then this will run.
         screen.fill((255,255,255)) #Placeholder
      elif return_pressed==2: #If the enter key is pressed twice, this will be drawn.
         screen.blit(controls, controls_location) #The controls are displayed on the screen.
      else: #Otherwise, this will run.
         set_score=True #set score is set to true.
   pygame.display.update() #Screen is refreshed.
   
   if set_score: #if set score is set to true, this will run.
         goal_display = font.render(f"Set Goal - {goal_input}", True, "Green") #The goal being inputted is continously updated on the screen.
         goal_display_parameters=goal_display.get_rect(topleft=(300,100)) #The goal the user inputs is put into a rect.
         goal_display_2 = font_2.render("Press enter to start the game!", True, "Green") #The goal being inputted is continously updated on the screen.
         goal_display_parameters_2=goal_display_2.get_rect(topleft=(375,700)) #The goal the user inputs is put into a rect. 
         screen.fill((0, 0, 0)) #background filled with black
         screen.blit(goal_display,  goal_display_parameters)  # Positions score on the scrren.
         screen.blit(goal_display_2, goal_display_parameters_2)
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
                  if event.unicode.isdigit() and len(goal_input) < 7:  #If the inputted key is a digit and is smaller than a million this will run.
                     goal_input += event.unicode  # Adds the digit to string
                  elif event.key == pygame.K_BACKSPACE: #If the key is backspace, then a digit must be removed.
                     goal_input = goal_input[:-1]  # Allows deletion, copilot given.
                  elif event.key==pygame.K_RETURN and not goal_input=="": #They are ready to play the game.
                     goal=int(goal_input) #Converts the goal string to an int for a later comparison.
                     splash_screen=False #The spalsh screen is false.
                     set_score=False #set score is set to false
                     main_game=True #The main game can now run.
                     goal_stored=goal #The new goal stored is the goal the user inputted.
   
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
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and special_speed_counter > 0: #This is where get pressed comes into play, because event key can only...
               #register one event at a time.
               player_speed = -30 #Player moves way faster than the bull to the left.
               special_speed_counter-=1 #One of the special dashes is removed from the user.
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and special_speed_counter > 0: #Same as above but for right movement.
               player_speed = +30 #Player moves way faster than the bull to the right.
               special_speed_counter-=1  #One of the special dashes is removed from the user.
            if event.key==pygame.K_w or event.key==pygame.K_SPACE or event.key==pygame.K_UP: #If the key pressed is w or space or up, this happens.
               player_gravity = -23 #Player gravity is set to -23, which is tied to the y movement.
            if event.key==pygame.K_s or event.key==pygame.K_DOWN: #If the s or down is pressed this will run.
               player_gravity = +30 #Player gravity is set to 30, which is  also tied to the y movement.
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
         goal_display = font_3.render(f"Set A New Goal - {goal_input}", True, "Green") #The goal being inputted is continously updated on the screen.
         goal_display_parameters=goal_display.get_rect(topleft=(0,0)) #The goal the user inputs is put into a rect.
         goal_display_2 = font_2.render("Press enter to start the game!", True, "Green") #Prompts the user to continue the game.
         goal_display_parameters_2=goal_display_2.get_rect(topleft=(375,1000)) #The goal the user inputs is put into a rect. 
         previous_score=font_2.render(f"Previous: {goal_stored}", True, "Green") #The previous score the user attempted is displayed on the screen.
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
            if event.unicode.isdigit() and len(goal_input) < 7:  #If the inputted key is a digit and is smaller than a million this will run.
               goal_input += event.unicode  # Adds the digit to string
            elif event.key == pygame.K_BACKSPACE: #If the key is backspace, then a digit must be removed.
               goal_input = goal_input[:-1]  # Allows deletion, copilot given.
            elif event.key==pygame.K_RETURN and not goal_input=="": #They are ready to play the game.
               score=0 #Score is set to 0 
               player_hitbox.y=starting_pos #Allows the player to not collide with th ebull when the game starts
               player_speed=0 #Prevents left over horizontal movement.
               points_text=font_2.render("Points: 0 ", True, "White") #Points are reset to 0.
               points_text_box=points_text.get_rect(topleft=(0,0))
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
               warning_y=random.randint(starting_pos - 540, SCREEN_HEIGHT-360) #A random y for the warning is chosen.
               projectile_x=warning_x #Projectile x is set to the value of warning x.
               projectile_y=warning_y #Projectile y is set to the value of warning y.
               #projectile_location=projectile.get_rect(topleft=(projectile_x, projectile_y))
               warning_checked=0 #Warning checked is set to 0.
      else: #This took an extremely long time to figure out, but I cracked it after two days.
               #Literally, just draw the game over screen here instead of using a function and if the user presses enter then set the game_over flag to false which
               #would trigger the above code to run.
               #Seriously, it was that easy, I'm glad I was able to figure out through trial and error.
               score_game_over=str(score) #I was able to Fix the issue where score was going up on key up, I had to basically like just make the score be at outside of the main loop
               #since it used to be a local variable, so now it works.
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
         bull_dice_roll=random.randint(0,1) #Chooses between 0 and 1 to avoid weird movement that caused the bull to move in a circle.
         if bull_dice_roll==0: #If the bull dice roll is 0
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
        points_text=font_2.render("Points " + score, True, "White") #A rect object that contains the updated score is made.
        points_text_box=points_text.get_rect(topleft=(0, 0)) #Sets the points location on the screen.
        if int(score) >= goal: #A score to win will be determined. For now, it is set to 10.
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
     screen.blit(player_256, player_hitbox) #Player drawn onto the screen.
     screen.blit(bull, bull_hitbox) #The bull is drawn on the screen.

     #YOU MUST FIGURE OUT HOW TO AVOID THE ITEMS FROM SPAWNING WHERE THE BULL IS, SO YOU MUST CHECK THAT THE item and bull hitbox .left and .right do not intersect otherwise it would be very unfair for the player.
     if current_time - item_last_seen >= item_respawn_cooldown: #If the time elapsed is greater than the cooldown this will run.
        while True: #This loop will continously generate x and y value  for the item until there is no overlap with the bull.
               item_x_pos=random.randint(200,1581) #Remember, you need to subtract the width and the height of the object to prevent it from going off the screen
               item_y_pos=random.randint(200,550) #Remember, you need to subtract the width and the height of the object to prevent it from going off the screen
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
        water_location_select=random.choice(water_possible_locations)
        water_puddle_last_seen=current_time #The water puddle hazard would last be seen at that time.
        water_puddle_x=water_location_select#Water puddle_x is tthen set to be at this location. Default 100 to SCREEB_WIDTH  - 350 #REWORKED FOR BETTER LOGIC
        water_puddle_y=starting_pos - 100 #Water puddle y location is set.
        water_puddle_location.topleft=(water_puddle_x, water_puddle_y) #Water puddle is drawn at this location.
        water_possible_locations_2=[785, SCREEN_WIDTH-350] #The water puddle facing right can be at these locations.
        water_location_select_2=random.choice(water_possible_locations_2) #A random choice is made to select the location to draw the water.
        water_puddle_x_2=water_location_select_2 #The water puddles x location is the one that was randomly chosen.
        water_puddle_y_2=starting_pos-100 #Water puddle's y location is set here.
        water_puddle_location_2.topleft=(water_puddle_x_2, water_puddle_y_2) #The water puddle will be drawn at this location.
        print(water_puddle_x) #For debug purposes.
        water_puddle_cooldown=random.randint(5000,10000) #Water puddle cooldown is reset.
     if not bull_charging and current_time - bull_last_seen >= bull_movement_cooldown: #If the bull has not moved in a certain amount of time and the bull is not currently charging this will run.
        bull_lock_on() #Calls the bull lock on function.
     if inner_loop_x: #If the inner loop is true, this will run.
        if bull_hitbox.x < player_hitbox.x: #If the bull is in a position left of the player, it must move right.
           bull_speed=17 #Bull speed is set to 17.
           bull_hitbox.x += bull_speed  # Moves the bull to the right of the screen.
        elif bull_hitbox.x > player_hitbox.x: #If the bull is to the right of the player, it must move to the left.
             bull_speed=17 #Bull speed is set to 17.
             bull_hitbox.x -= bull_speed # Moves the bull to the left of the player.
        else: #Otherwise, if the bull is neither to the left or right of the player, then it is assumed that the bull and the player are the same x location.
              inner_loop_x = False  #Bull does not need to move, so inner_loop boolean is set to false.
              inner_loop_y = True #The inner loop y is set to true to make the bull follow the player across the y axis
             # points_text_box=points_text.get_rect(topleft=(600, 100)) #Sets the points location on the screen.
     if inner_loop_y: #If the inner loop is true, this will run.
        if bull_hitbox.y < player_hitbox.y :#If the bull is higher than the player, then it must be brought down.
             bull_hitbox.y += 25 # Moves the bull to the bottom of the screen 25 is default
        elif bull_hitbox.y > player_hitbox.y: #If the bull is to the bottom of the player, it must move up.
             bull_hitbox.y -= 32 # Moves the bull to the top of the screen.
        else: #Otherwise, if the bull is neither to the left or right of the player, then it is assumed that the bull and the player are the same y location.
              inner_loop_y = False  #Bull does not need to move, so inner_loop boolean is set to false.
              bull_charging=False #Bull charging is set to false, which means the cooldown can work properly now.
     if bull_hitbox.colliderect(item_hitbox) and points >= 20: #if the bull collides with the item, this will happen.
        item_hitbox.y=10000 # The item will move out the way
        points-=20 #The points get reduced by 20.
        points_text=font_2.render(f"Bull Got Item...-20 POINTS!", True, "RED") #Removes the points and displays on screen
        points_text_box=points_text.get_rect(topleft=(0,0)) #The goal the user inputs is put into a rect. 
        print("The bull got this item!") #For debug purposes.
     if bull_hitbox.colliderect(player_hitbox): # If the bull touches the player this will happen.
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
     time_message=font_2.render("Stopwatch in Minutes", 'True', 'White')
     time_message_textbox=time_message.get_rect(topleft=(1160,0))
     if time_keep: #as long as the timer is set to ne true, this will run.
        seconds=int((pygame.time.get_ticks() - starting_time_secs)/1000) #The seconds are stored seperately to allow a reset of the seconds, but not the minutes.
        if seconds >= 60:#To prevent the seconds from ticking up again.
           starting_time_secs=pygame.time.get_ticks() #Resets the seconds to start back at 0.
        current_time_disp=font_2.render("MIN " + str(int((pygame.time.get_ticks() - starting_time)/60000)) + "                         SEC " + str(seconds), 'True', 'White') #The clock is shown on the screen, wrapped in multiple braces to avoid weird clock issues.
        total_time=str(int((pygame.time.get_ticks() - starting_time)/60000)) + " M " + str(seconds) + " S" #The total time is stored, which is useful for the game over and mission accomplished screens.
        current_time_textbox=current_time_disp.get_rect(topleft=(1160,60)) #places the timer on the specific location on screen.
        screen.blit(current_time_disp, current_time_textbox) #The time is shown on the screen.
     if current_time - projectile_last_seen > projectile_cooldown: #FINALLY, AFTER A WHOLE 3 DAYS, THIS WORKS! Timer used to determined if projectile ready to be shown.
        #warning_location=warning.get_rect(topleft=(warning_x, warning_y)) # A warning is ready to be shown at this location.
        #The issue was that warning x was getting reassigned even wit the projectile active boolean set to false.
        #This caused the projectile to be drawn on the screen twice incorrectly.
        warning_active=True #Flag that the warning is active is set to true.
     if warning_active: #If the warning is active this will run.
        #screen.blit(warning, warning_location) #Warning drawn on this location on the screen.
        warning_checked+=1 #Warning checked gets 1 added, this allows the time to be checked precisely ONCE!
        if warning_checked > 0 and warning_checked < 2: #Provided warning checked is greater than 0 and less than two, this will run.
           print("Comparison reached") #Prints that the comparison was reached
           warning_last_seen=pygame.time.get_ticks() #Time checked precisely once rather than having to reset it.
           warning_x=0 #Warning_x is also set to 0 precisely once, which prevents an issue whre the x would constantly be set to 0
           #which prevented the comparison later to not work.
           print(str(warning_last_seen) + " was last seen at this time.") #For debug purposes.
        if current_time - warning_last_seen > warn_window: #If the warning has passed 5 seconds, the projectile can now be shown.
            projectile_active=True #Projectile active is now set to true.
            #print("projectile can now be shown.")
     if projectile_active: #If the projectile_active is true, this can run.
        warning_active=False #The warning is no loner active
        projectile_x+=15 #Projectile will move across the x axis at this rate.
        #if projectile_x <= 1920: #If the proectile is not off the screen, this can run.
            #projectile_location=projectile.get_rect(topleft=(projectile_x, projectile_y)) #Projectile is placed at this location.
            #screen.blit(projectile, projectile_location) #Projectile drawn at this location.
        #else: #If the projectile is off the screen this will run.
            #projectile_active=False #Projectile active is set to false.
            #print("The projectle is now deactived.") #For debug
            #projectile_last_seen=current_time #Projectile last seen is set to current time.
            #warning_y=random.randint(starting_pos - 540, SCREEN_HEIGHT-360) #The warning's y location is set to a random location, this also serves as the y location for the projectile.
            #projectile_x=warning_x #Projectile x location is set to the warning's x location.
            #projectile_y=warning_y #Projectile's y location is set to the warning's y location.
            #projectile_cooldown=random.randint(5000,10000) #The cooldown is reset.
            #  warning_checked=0 #Warning checked is equal to 0.
     bull_gravity+=1 #Brings the bull back to the ground.
     bull_hitbox.y+=bull_gravity #Bull moves accordingly to the increasing gravity.
     player_sprites() #Sprites for player function called.
     screen.blit(item, item_hitbox) #item is drawn on the screen.
     screen.blit(water_puddle, water_puddle_location) #The water puddle facing left is drawn on screen.
     screen.blit(water_puddle_2, water_puddle_location_2) #The water puddle facing right is drawn on screen.
     screen.blit(points_text, points_text_box) #points are displayed on the screen.
     screen.blit(time_message, time_message_textbox) #The timer is displayed on screen.
     #screen.blit(current_time, current_time_textbox) #The time is shown on the screen.
     pygame.display.update() #Screen is refreshed
     clock.tick(60) #Frame rate is set to a max of 60.
   



