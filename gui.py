import pygame
import sys
from pygame.locals import *
import statistics as st
import numpy as np 
import tensorflow as tf 
from keras.models import load_model
import cv2


pygame.init()
pygame.display.set_caption('MNIST GUI')
WIDTH, HEIGHT = 900, 900
FPS = 60
white = (255, 255, 255)
dark_white = (209, 171, 171)
blue = (0, 0, 128)
red = (255,0,0)
dark_red = (180, 0, 0)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont('freesansbold.ttf', 60)

Numbers = {0:"Zero", 1:"One", 2:"Two", 
           3:"Three", 4:"Four", 5:"Five",
           6:"Six", 7:"Seven", 8:"Eight",
           9:"Nine"}

model = load_model("mnist.h5")



def makeText(text, color1, color2, surface, x, y, fontSize):
    font = pygame.font.SysFont('freesansbold.ttf', fontSize)
    msg = font.render(text, True, color1, color2)
    # msg, textRect = text_objects(msg, font)
    textRect = msg.get_rect()
    textRect.center = (x, y)
    surface.blit(msg, textRect)
    return 

def main_menu():
    click = False
    running = True
    clock = pygame.time.Clock()
    clock.tick(FPS)
    screen.fill((0,0,0))
    makeText('Main Menu', white, blue,screen, WIDTH//2, HEIGHT - 675, 60)
    
    while running:
        mx, my = pygame.mouse.get_pos()
        
        button1 = pygame.Rect(100,350,200,50)
        if 100 < mx < 100+200 and 350 < my < 350 + 50:
            pygame.draw.rect(screen,dark_red,button1)
            makeText('MNIST', dark_white, None, screen,st.mean([100,100+200]),st.mean([350,350+50]), 45)
        else:
            pygame.draw.rect(screen,red,button1)
            makeText('MNIST', white, None, screen,st.mean([100,100+200]),st.mean([350,350+50]), 45)
        
        button2 = pygame.Rect(362.5,350,200,50)
        if 362.5 < mx < 362.5+200 and 350 < my < 350 + 50:
            pygame.draw.rect(screen,dark_red,button2)
            makeText('About', dark_white, None, screen,st.mean([362.5,362.5+200]),st.mean([350,350+50]), 45)
        else:
            pygame.draw.rect(screen,red,button2)
            makeText('About', white, None, screen,st.mean([362.5,362.5+200]),st.mean([350,350+50]), 45)
        
        button3 = pygame.Rect(625,350,200,50)
        if 625 < mx < 625+200 and 350 < my < 350 + 50:
            pygame.draw.rect(screen,dark_red,button3)
            makeText('Quit', dark_white, None, screen,st.mean([625,625+200]),st.mean([350,350+50]), 45)
        else:
            pygame.draw.rect(screen,red,button3)
            makeText('Quit', white, None, screen,st.mean([625,625+200]),st.mean([350,350+50]), 45)
        
        if button1.collidepoint((mx,my)):
            if click:
                mnist()
        if button2.collidepoint((mx,my)):
            if click:    
                about()
        if button3.collidepoint((mx,my)):
            if click:    
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == True:
                    click = True
            pygame.display.update()
tempX = []
tempY = []
def mnist():
    click = False
    writing = False
    running = True
    pred =  True
    clock = pygame.time.Clock()
    clock.tick(FPS)
    screen.fill((0,0,0))
    x_tracker = []
    y_tracker = []
    while running:
        makeText('MNIST MODEL IN ACTION', white, blue, screen, WIDTH//2, HEIGHT - 675, 60)
        mx, my = pygame.mouse.get_pos()

        return_button = pygame.Rect(30, 30, 100,50)
        if 30 < mx < 30 + 100 and 30 < my < 30 + 50:
            pygame.draw.rect(screen, dark_red, return_button)
            makeText('Main Menu', dark_white, None, screen, st.mean([30,30+100]), st.mean([30, 30+50]), 25)
        else:
            pygame.draw.rect(screen, red, return_button)
            makeText('Main Menu', white, None, screen, st.mean([30,30+100]), st.mean([30, 30+50]), 25)
        
        next_button = pygame.Rect(770, 30, 100,50)
        if 770 < mx < 770 + 100 and 30 < my < 30 + 50:
            pygame.draw.rect(screen, dark_red, next_button)
            makeText('About', dark_white, None, screen, st.mean([770, 770+100]), st.mean([30, 30+50]), 25)
        else:
            pygame.draw.rect(screen, red, next_button)
            makeText('About', white, None, screen, st.mean([770,770+100]), st.mean([30, 30+50]), 25)

        clear_button = pygame.Rect(st.mean([30,770]), 30, 100, 50)               
        if st.mean([30,770]) < mx < st.mean([30,770]) + 100 and 30 < my < 30 + 50:
            pygame.draw.rect(screen, dark_red, clear_button)
            makeText('Clear', dark_white, None, screen, st.mean([st.mean([30,770]), st.mean([30,770]) +100]), st.mean([30, 30+50]), 25)
        else:
            pygame.draw.rect(screen, red, clear_button)
            makeText('Clear', white, None, screen, st.mean([st.mean([30,770]), st.mean([30,770]) +100]), st.mean([30, 30+50]), 25)


        if return_button.collidepoint((mx,my)):
            if click:
                main_menu()
        if next_button.collidepoint((mx,my)):
            if click:
                about()
        if clear_button.collidepoint((mx,my)):
            if click:
                screen.fill((0,0,0))
        
        
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEMOTION and writing:
                mx, my = event.pos
                pygame.draw.circle(screen, red, (mx,my),4,0)

                
                x_tracker.append(mx)
                y_tracker.append(my)

            if event.type == MOUSEBUTTONDOWN:
                if event.button == True:
                    click = True
                writing = True
            if event.type == MOUSEBUTTONUP:
                writing = False
                if len(x_tracker) != 0 and len(y_tracker) != 0:
                    y_tracker = sorted(y_tracker)
                    x_tracker = sorted(x_tracker)
                
                
                
                    # Draw Rect around drawing
                    
                    min_x, max_x = max(x_tracker[0] - 20,0), min(x_tracker[-1] + 20,WIDTH)
                    min_y, max_y = max(y_tracker[0] - 20,0), min(y_tracker[-1] + 20, HEIGHT)
                    
                    print("Min X is ",min_x)
                    print("Max X is ",max_x) 

                    print("Min y is ", min_y)
                    print("Max y is ", max_y)
                    print(" ")

                    # Empty out array for future mouse inputs 
                    x_tracker = []
                    y_tracker = []

                    # Surface array which captures sufrace within 20px from all (x,y) points
                    recogniton = np.array(pygame.surfarray.array2d(screen)[min_x:max_x, min_y:max_y]).T.astype("float32")
        
                    # Incorpoate deep learning model to make a predition by returning the aasociated number
                    # with the highest probabilty
                                
                    if pred:
                        image = recogniton
                        img = cv2.resize(image,(28,28))
                        prediction = model.predict(img.reshape((1,28,28,1)))
                        number = (np.argmax(prediction, axis = 1))
                        print(Numbers[number[0]])
                    
                        num = Numbers[number[0]]

                        # Display the number above each drawing 
                        num_display = font.render(num, True, red, blue)
                        text_rect = num_display.get_rect()
                        text_rect.left = min_x
                        text_rect.bottom = min_y
                        screen.blit(num_display,text_rect)
                        pygame.draw.rect(screen, dark_red, (min_x,min_y,max_x - min_x, max_y - min_y), 5)

                        
                        
                    
                    
            
        pygame.display.update()

def about():
    click = False
    running = True
    screen.fill((0,0,0))
    while running:
        makeText('About the Mnist Data Set', white, blue, screen, WIDTH//2, HEIGHT - 675, 60)
        mx, my = pygame.mouse.get_pos()
        
        return_button = pygame.Rect(30, 30, 100,50)
        if 30 < mx < 30 + 100 and 30 < my < 30 + 50:
            pygame.draw.rect(screen, dark_red, return_button)
            makeText('Main Menu', dark_white, None, screen, st.mean([30,30+100]), st.mean([30, 30+50]), 25)
        else:
            pygame.draw.rect(screen, red, return_button)
            makeText('Main Menu', white, None, screen, st.mean([30,30+100]), st.mean([30, 30+50]), 25)
        
        next_button = pygame.Rect(770, 30, 100,50)
        if 770 < mx < 770 + 100 and 30 < my < 30 + 50:
            pygame.draw.rect(screen, dark_red, next_button)
            makeText('MNIST', dark_white, red, screen, st.mean([770, 770+100]), st.mean([30, 30+50]), 25)
        else:
            pygame.draw.rect(screen, red, next_button)
            makeText('MNIST', white, red, screen, st.mean([770,770+100]), st.mean([30, 30+50]), 25)

        if return_button.collidepoint((mx,my)):
            if click:
                main_menu()
        if next_button.collidepoint((mx,my)):
            if click:
                mnist()
        
        click = False
        
        makeText("Hello my name is abbas kazmo and i will be explaing to you what exactly the mnist model is and how i got it to"
        , white, None, screen, 450,450, 35 )
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == True:
                    click = True
        pygame.display.update()

main_menu() 
