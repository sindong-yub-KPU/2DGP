from pico2d import *
open_canvas()
import math
grass = load_image("grass.png")
character = load_image('character.png')
circle_x = 400
circle_y = 300
x= 0;
y= 30;
count =0 ;
seta = 3.14;
while(True):
    
    if(count == 0):
        
        
        while (x < 790):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, 90)
            x = x + 5
            delay(0.01)
            if(x >= 790):
                count = 1
                y=90
          
            
    if(count == 1):
        
        
        while(y < 570):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            y = y + 5
            delay(0.01)
            if(y >= 570):
                count = 2
    if(count == 2):
        
        
        while(x > 10):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            x = x - 5
            delay(0.02)
            if(x <= 10):
                count = 3         
    if(count == 3):
        
        
        while(y > 90):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            y = y - 5
            delay(0.01)
            if(y >= 90):
                count = 4         
    if(count == 4):
        
        
        while(x < 400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            x = x + 5
            delay(0.02)
            if(x== 400):
                count = 5     
    if(count == 5):
        
        
        while(True):
            
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, y)
            x =400 + 250*math.sin(seta)
            y =300 + 200*math.cos(seta)
            if ( seta  >= 9.42):
                seta = 3.14
                x = 400
                count = 0
                break
            seta = seta + 0.0314
            print(seta)
            delay(0.01)
           
            
            
    



close_canvas()
