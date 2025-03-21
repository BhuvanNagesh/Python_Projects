print("How many canes of Paint is needed?")

def paint_calc (height, width, cover):  
    area= height*width
    num_of_cans= round(area/cover)
    print(f"You'll need {num_of_cans} cans of paint.")  
    
height= float(input("Enter the height of the wall: "))
width= float(input("Enter the width of the wall: "))
cover= 5

paint_calc(height, width, cover)