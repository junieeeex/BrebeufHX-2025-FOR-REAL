from random import shuffle
import pygame
import sys
import numpy as np
import time
from Kw import Kw
import os
from pygame.locals import *
pygame.init()

screen_width = 400
screen_height = 800
Times_font = pygame.font.SysFont("markerfelt", 32)
screen = pygame.display.set_mode((screen_width, screen_height))

BEIGE = (245,230,210)
DARK_BURGANDY = (200, 76, 5)
LIGHT_BURGANDY = (223,109,45)
GREEN = (99,140,109)
TEAL = (231, 251, 180)


class Button:
    def __init__(self, x,y, width, height, text, color, action=None):
        self.rect = pygame.Rect(x,y,width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw (self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = Times_font.render (self.text, True, (255,255,255))
        surface.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                    self.rect.y + (self.rect.height -text_surface.get_height()) // 2 ))
        
    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)
    
    def click(self):
        if self.action:
            self.action()

class InputBox:
    def __init__(self, x, y, w, h, prompt = "Entrez une température"):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (DARK_BURGANDY)
        self.text = ''
        self.txt_surface = Times_font.render(self.text, True, (DARK_BURGANDY))
        self.active = False
        self.prompt = prompt
        self.input_value = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                elif event.key == pygame.K_RETURN:
                   pass
                   
                else:
                    self.text += event.unicode
                self.txt_surface = pygame.font.SysFont("markerfelt", 20).render(self.text, True, (GREEN))

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))


#input temp
input_box1 = InputBox(100, 350, 200, 32)

def go_to_preferred_distance():
    global current_state
    current_state = PREFERRED_DISTANCE_PAGE

def go_to_main_menu():
    global current_state
    current_state = MAIN_MENU

def go_to_front_page():
    global current_state
    current_state = FRONT_PAGE

def go_to_tags():
    global current_state
    current_state = TAGS_PAGE

def go_to_restaurants():
    global current_state
    current_state = RESTAURANTS_PAGE

def get_distance():
    global input_distance
    input_distance = input_box1.text
    if input_box1.input_value:
        try:
            input_distance = float(input_box1.input_value)
        except ValueError:
            print("invalid input")
        print("Input distance:", input_distance)

    return input_distance


def function_next1_button():
    get_distance()
    input_box1.active = False
    go_to_main_menu()

draw_check_green = False
draw_check_red = False
show_image = True
row = 0

def update_row():
    global row
    row += 1

def check_image_green():
    global draw_check_green, show_image
    draw_check_green = True
    show_image = False
    update_row()
    show_image = True


def check_image_red():
    global draw_check_red, show_image
    draw_check_red = True
    show_image = False
    update_row()
    show_image = True


input_distance = get_distance()
        

next1_button = Button(150, 500, 100, 40, "Next", (GREEN) ,function_next1_button)
next2_button = Button(75, 300, 250, 300, "Start Swiping!", (GREEN), go_to_front_page)
next3_button = Button( 170, 700, 60, 40, "Next", (0,0,0), go_to_tags)
next4_button = Button( 20, 500, 60, 20, "Next", (0,255,0), go_to_restaurants)

yes_button = Button(300, 625, 60, 40, "Yes!", (GREEN), check_image_green)
no_button = Button(40, 625, 60, 40, "No!", (LIGHT_BURGANDY), check_image_red)

PREFERRED_DISTANCE_PAGE = 1
MAIN_MENU = 2
FRONT_PAGE = 3
TAGS_PAGE = 4
RESTAURANTS_PAGE = 5


current_state = PREFERRED_DISTANCE_PAGE

photo_list_tag = [
    ['hamburgerrr.PNG', "american food","fast food"],
    ['fries.PNG',  "american food","fast food"],
    ['chicken_fried.PNG', "american food","fried chicken","fast food"],
    ['hotdog.PNG', "american food","hot dog","fast food"],
    ['beef?.PNG', "korean food",],
    ['bibimbap.PNG', "korean food"],
    ['koreanfriedchicken.PNG', "korean food"],
    ['kimbap.PNG', "korean food"],
    ['armysoup.PNG', "korean food"],
    ['matchawaffles.PNG', "cafe","bakery"],
    ['cupcakes.PNG', "cafe","bakery"],
    ['carrotcake.PNG', "cafe","bakery"],
    ['icecoffee.PNG', "cafe"],
    ['matchalatte.PNG', "cafe"],
    ['mangostickyrice.PNG', "thai food"],
    ['shrimp.PNG', "thai food"],
    ['gingerthing.PNG', "thai food"],
    ['eggchicken.PNG', "thai food"],
    ['bols.PNG', "thai food"],
    ['padthai.PNG', "thai food"],
    ['redcurry.PNG', "indian food"],
    ['pate.PNG', "indian food"],
    ['mix.PNG', "indian food"],
    ['samosa.PNG', "indian food"],
    ['ballz.PNG', "indian food"],
    ['burrito.PNG',"mexican food"],
    ['nachos.PNG', "mexican food"],
    ['tacos.PNG', "mexican food"],
    ['softtaco.PNG', "mexican food"],
    ['guac.PNG', "mexican food"],
    ['hotpot.PNG', "chinese food"],
    ['weirdbol.PNG', "chinese food"],
    ['dimsum.PNG', "chinese food"],
    ['dumplings.PNG', "chinese food"],
    ['sushi.PNG', "japanese food"],
    ['tempura.PNG', "japanese food"],
    ['onigiri.PNG', "japanese food"],
    ['okonomyaki.PNG', "japanese food"],
    ['ramen.PNG', "japanese food","noodles"],
    ['pizza.PNG', "pizza","italian food"],
    ['pasta.PNG', "italian food"],
    ['gelato.PNG', "italian food","ice cream"],
    ['risotto.PNG', "italian food"],
    ['chocolate.PNG', "italian food","baked goods"]
]
shuffle(photo_list_tag)

def draw_red():
    pygame.draw.rect(screen, (LIGHT_BURGANDY), pygame.Rect(50, 200, 300, 400))
    pygame.draw.line(screen, (255,255,255), (100, 300), (300,500), 10)
    pygame.draw.line(screen, (255,255,255), (300, 300), (100,500), 10)

def draw_green():
    pygame.draw.rect(screen, (GREEN), pygame.Rect(50, 200, 300, 400))
    pygame.draw.line(screen, (255,255,255), (150, 400), (200, 450), 10)
    pygame.draw.line(screen, (255,255,255), (200, 450), (220, 350), 10)


def main():
    global draw_check_green
    global draw_check_red
    global row
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Hot dishes in your area")
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            input_box1.handle_event(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_state == PREFERRED_DISTANCE_PAGE:
                    if next1_button.is_hovered(event.pos):
                        next1_button.click()
                        pygame.display.update()
                    
                elif current_state == MAIN_MENU:
                    if next2_button.is_hovered(event.pos):
                        next2_button.click()
                        pygame.display.update()

                elif current_state == FRONT_PAGE:
                    if next3_button.is_hovered(event.pos):
                        next3_button.click()
                    elif yes_button.is_hovered(event.pos):
                        yes_button.click()
                    elif no_button.is_hovered(event.pos):
                        no_button.click()
                        pygame.display.update()

                elif current_state == TAGS_PAGE:
                    if next4_button.is_hovered(event.pos):
                        next4_button.click()
                        pygame.display.update()
                

    

               
                
            if current_state == PREFERRED_DISTANCE_PAGE:
                screen.fill((DARK_BURGANDY))
                pygame.draw.rect(screen, (BEIGE), pygame.Rect(20, 20, 360, 760))
                label1 = Times_font.render("Your preferred distance", 1, (GREEN))
                screen.blit(label1,(45,200))
                label2 = Times_font.render("(m)", 1, (GREEN))
                screen.blit(label2, (310, 350))
                next1_button.draw(screen)
                input_box1.update()
                pygame.display.flip()

            elif current_state == MAIN_MENU:
                screen.fill((DARK_BURGANDY))
                pygame.draw.rect(screen, (BEIGE), pygame.Rect(20, 20, 360, 760))
                label2 = Times_font.render("Welcome to", 1, (DARK_BURGANDY)) 
                label1 = Times_font.render("Hot Dishes in Your Area!",1, (DARK_BURGANDY))
                screen.blit(label2,(120,130))
                screen.blit(label1, (50,175))
                next2_button.draw(screen)
                pygame.display.flip()

            elif current_state == FRONT_PAGE:
                screen.fill((DARK_BURGANDY))
                pygame.draw.rect(screen, (BEIGE), pygame.Rect(20, 20, 360, 760))
                label1 = Times_font.render("front page", 1, (0,0,0))
                screen.blit(label1,(10,10))
                next3_button.draw(screen)
                no_button.draw(screen)
                yes_button.draw(screen)
                if show_image:
                    image = photo_list_tag[row][0]
                    tag = photo_list_tag[row][1:]
                    photo = pygame.image.load(image)
                    resized_image = pygame.transform.scale(photo, (300, 400))
                    screen.blit(resized_image, (50,200))

                    pygame.display.flip()
                    if draw_check_green:
                        if Kw.add_count_by_name(tag):
                            draw_match()
                        else: draw_green()
                        pygame.display.update()
                        pygame.time.wait(500)
                        draw_check_green = False
                        pygame.display.update()
                        pygame.display.flip()
                        
                    elif draw_check_red == True:
                        draw_red()
                        pygame.display.update()
                        pygame.time.wait(500)
                        draw_check_red = False
                        pygame.display.update()
                        pygame.display.flip()
                    
                            
                
            
                
    
            elif current_state == TAGS_PAGE:
                matches = Kw.get_matches() # These are Keyword objects but it'll return as strings if you just use them
                
                screen.fill((DARK_BURGANDY))
                pygame.draw.rect(screen, (BEIGE), pygame.Rect(20, 20, 360, 760))
                label1 = Times_font.render("Your Tags", 1, (0,0,0))
                screen.blit(label1,(10,10))
                next4_button.draw(screen)
                pygame.display.flip()
            
            elif current_state == RESTAURANTS_PAGE:
                screen.fill((DARK_BURGANDY))
                pygame.draw.rect(screen, (BEIGE), pygame.Rect(20, 20, 360, 760))
                label1 = Times_font.render("Restaurants!", 1, (0,0,0))
                screen.blit(label1,(10,10))
                pygame.display.flip()

            

    pygame.quit()



main()

print(input_distance)


