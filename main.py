import pygame
from sys import exit
import os
import openai
import random
from dotenv import load_dotenv
import button
import time

from ai_text_create import return_text_and_choice as ai_text
from ai_text_create import given_input_return_text_and_choice as ai_text_from_previous
from wrap_text import drawText as wrap_text_and_draw
from ai_image_create import make_image_and_save as ai_image



textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3
#all these are choices for the wrap_text function

textRect = pygame.Rect(100, 100, 300, 300)
#drawing a rectangle that the wrap_text function will sense and put the text inside of


pygame.init()

#define colours
TEXT_COL = ("White")

file2 = open("previous_day_story_and_choices.txt", "w+") 

#create game window
SCREEN_WIDTH = 1030
SCREEN_HEIGHT = 595
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

def loading_screen():
    screen.fill("Red")
    loading1 = pygame.image.load("graphics/loading1.png")
    loading2 = pygame.image.load("graphics/loading2.png")
    loading3 = pygame.image.load("graphics/loading3.png")
    screen.blit(loading1, (0,0))
    pygame.display.update()
    time.sleep(1)
    screen.blit(loading2, (0,0))
    pygame.display.update()
    time.sleep(.5)
    screen.blit(loading3, (0,0))
    pygame.display.update()
    time.sleep(.25)
    pygame.display.update()
    
loading_screen()

#game variables
game_paused = False
menu_state = "main"

#load button images

option1_img = pygame.image.load("graphics/option1.png").convert_alpha()
option1_img = pygame.transform.scale(option1_img, (150, 50))
option2_img = pygame.image.load("graphics/option2.png").convert_alpha()
option2_img = pygame.transform.scale(option2_img, (150, 50))
quit_img = pygame.image.load("graphics/button_quit.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img, (125, 50))

textRect = pygame.Rect(512, 0, 512, 512)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.SysFont("arialblack", 20)
#test_font = pygame.font.Font('font/game_over.ttf', 50)

#create button instances
option1_button = button.Button(287, 550, option1_img, 1)
option2_button = button.Button(559, 550, option2_img, 1)
quit_button = button.Button(437, 550, quit_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))




day1_text = ai_text() 
#produces the random text from the year

"""day1_text = 'The year is 7046 BC .\n\nYou wake up and get out of bed. \
You stretch and yawn as you make your way to the window. You open\
the curtains and see that the sun is just starting to rise. You \
can hear the birds singing and the leaves rustling in the breeze. \
You take a deep breath and feel the fresh air fill your lungs. You\
feel happy and alive.\n\nChoice 1: You decide to go for a walk \
outside and explore the world.\nChoice 2: You decide to stay inside\
and read a book.'
#this is for testing only
"""

#day2_text = 'Test worked!!'

#text_surface = font.render(day2_text, False, "Black")

ai_image(day1_text, "day1")  #generates an image from dalle. 
#The first parameter is the text that will inform the ai to create the picture
#The second parameter 

day1_image = pygame.image.load('graphics/day1.jpg')

played_count = 0
patience_scale = ""
next_text = None
run = True
while run:
    screen.fill((52, 78, 91)) 
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            run = False

    #check if game is paused
    if game_paused == True:
        #check menu state
        if menu_state == "main":
        #draw pause screen buttons
            pygame.draw.rect(screen, (0, 0, 0), textRect, 1)
            drawTextRect = textRect.inflate(-5, -5)
            screen.blit(day1_image, (0,0))
            wrap_text_and_draw(screen, day1_text, (0, 0, 0), drawTextRect, font, textAlignBlock, True)
            if option1_button.draw(screen):
                print("option1 chosen!!")
                loading_screen()
                menu_state = "option1"
                file1 = open('previous_day_story_and_choices.txt', 'w+')
                previous = file1.read()
                next_text = ai_text_from_previous(previous, "option 2 ")
                
                ai_image(next_text, "next_image")
                file1.write(next_text)
                # Closing file
                file1.close()
                played_count += 1
            if option2_button.draw(screen):
                
                print("option2 chosen!!")
                loading_screen()
                menu_state = "option2"
                file1 = open('previous_day_story_and_choices.txt', 'w+')
                previous = file1.read()
                next_text = ai_text_from_previous(previous, "option 2 ")
                ai_image(next_text, "next_image")
                file1.write(next_text)
                # Closing file
                file1.close()
                played_count += 1
            if quit_button.draw(screen):
                menu_state = "quit"
                
        #check if the option2 menu is open
        if menu_state == "option1":
            
            screen.fill("Red")
            next_image = pygame.image.load('graphics/next_image.jpg')
            pygame.draw.rect(screen, (0, 0, 0), textRect, 1)
            drawTextRect = textRect.inflate(-5, -5)
            screen.blit(next_image, (0,0))
            wrap_text_and_draw(screen, next_text, (0, 0, 0), drawTextRect, font, textAlignBlock, True)
            
            if option1_button.draw(screen):
                menu_state = "option1"
                print("option1 chosen!!")
                loading_screen()
                file1 = open('previous_day_story_and_choices.txt', 'w+')
                previous = file1.read()
                next_text = ai_text_from_previous(previous, "option 2 ")
                
                ai_image(next_text, "next_image")
                file1.write(next_text)
                # Closing file
                file1.close()
                played_count += 1
                
            if option2_button.draw(screen):
                print("option2 chosen!!")
                menu_state = "option2"
                loading_screen()
                file1 = open('previous_day_story_and_choices.txt', 'w+')
                previous = file1.read()
                next_text = ai_text_from_previous(previous, "option 1")
                ai_image(next_text, "next_image")
                file1.write(next_text)
                # Closing file
                file1.close()
                played_count += 1
                
                
            if quit_button.draw(screen):
                menu_state = "quit"
        if menu_state == "option2":
            
            screen.fill("Red")
            
            next_image = pygame.image.load('graphics/next_image.jpg')
            pygame.draw.rect(screen, (0, 0, 0), textRect, 1)
            drawTextRect = textRect.inflate(-5, -5)
            screen.blit(next_image, (0,0))
            wrap_text_and_draw(screen, next_text, (0, 0, 0), drawTextRect, font, textAlignBlock, True)
            if option1_button.draw(screen):
                print("option1 chosen!!")
                menu_state = "option1"
                loading_screen()
                file1 = open('previous_day_story_and_choices.txt', 'w+')
                previous = file1.read()
                next_text = ai_text_from_previous(previous, "option 2 ")
                ai_image(next_text, "next_image")
                file1.write(next_text)
                # Closing file
                file1.close()
                played_count += 1
                
            if option2_button.draw(screen):
                menu_state = "option2"
                print("option2 chosen!!")
                loading_screen()
                file1 = open('previous_day_story_and_choices.txt', 'w+')
                previous = file1.read()
                next_text = ai_text_from_previous(previous, "option 1")
                ai_image(next_text, "next_image")
                file1.write(next_text)
                # Closing file
                file1.close()
                played_count += 1
                
            if quit_button.draw(screen):
                menu_state = "quit"
        if menu_state == "quit":
            screen.fill("Red")
            if played_count <= 2:
                patience_scale = "You Are Impatient!!"
            elif 3 <= played_count <= 5:
                patience_scale = "You Are Somewhat Patient."
            elif 6 <= played_count <= 10:
                patience_scale = "You Are Patient."
            elif 11 <= played_count:
                patience_scale = "You Are Very Patient!!"
            draw_text("You Played " + str(played_count) + " Iterations." + str(patience_scale), font, TEXT_COL, 75, 250) 
    else:
        draw_text("Press SPACE play", font, TEXT_COL, 75, 250)   
    
    
    
    
    
    
    
    
    pygame.display.update()
    clock.tick(60)