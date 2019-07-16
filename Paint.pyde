def setup():
    size(512, 512)
    #noStroke()
def draw():
    if mousePressed :
        fill(140, 244, 255)
        draw_size = 100
        ellipse(mouseX - draw_size/2, mouseY - draw_size/2, draw_size, draw_size)
    if keyPressed and key == "c" or key == "C":
          background(200, 200, 200)
         # print(keyCode)
        
    
    
    
    
    #elif mouseY > 256 :
        #fill(0,500,0)
    # else : 
    #     fill(34,139,34) 
     
        # if mouseX > 256:
        #     fill(500,0,0)
        # else :
        #     fill(0,0,500) 

    
