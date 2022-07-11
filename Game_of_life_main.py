import Field_operator
import Field_explorer ##
import Windmodule

import time

import sys

def U_Interface_V2():
    global start_time
    start_time = time.time()

    print('Initiating program...')
    print('...')

    print('Setup: Please choose either \"standard\" or \"manual\" by typing your choice (Recommended: "standard").')
    trials = 1
    while trials <= 3:
        try:
            setup = input(">>")
            if(setup == 'standard' or setup == ''):
                trials = 4
                print("Standard settings selected.")
                Width = 600
                Height = 600
                length = 30
                Trimming = False
            elif(setup == "manual"):
                trials = 1
                while trials <= 3:
                    print("Please input the desired width and height of the canvas (same value) (Recommended: 600).")
                    try:
                        Width = int(input('>>'))
                        Height = Width

                        trials = 4
                    except:
                        print("An error occurred while inputing width and height.")
                        print("Please try again (Recommended: 600).")
                        trials += 1
                
                trials = 1
                while trials <= 3:
                    print('Please specify the number of squares on one side (Recommended: 30)')
                    try:
                        length = int(input('>>'))
                        trials = 4
                    except:
                        print('An error occurred while inputing the number of squares per side')
                        print('Please try again (Recommended: 30).')
                        trials += 1
                
                trials = 1
                while trials <= 3:
                    print('Please specify if "trimming" should be available ("yes" or "no") (Recommended: "no")')
                    
                    try:
                        Trimming = input('>>')
                        if(Trimming == "yes"):
                            Trimming == True
                        elif(Trimming == "no"):
                            Trimming = False
                        else:
                            raise Exception()
                        trials = 4
                    except:
                        print('An error occurred while inputing "trimming" setting')
                        print('Please try again (Recommended: "no")')
                        trials += 1
                
            else:
                raise Exception()
                    

        except:
            print('An error occurred while inputing, please try again.')
            trials += 1
    
    print("Setup completed")

    main_sheet = Field_operator.Create_random_field(length)
    Windcan = Windmodule.Windclass(Width, Height, "Simply: life")
    return main_sheet, Windcan, Trimming



#Method to let user manipulate settings of program
def U_Interface():
    
    global start_time
    start_time = time.time()
    
    print('Initiating program...')
    print('...')
    
    print('Setup: Manual or standard?')
    setup = input('>>')
    if (setup == 'standard' or setup == ''):
        Width = 600
        Height = 600
        length = 30
        Trimming = False
        
    elif(setup == 'Manual'):
        print('Width and Height of canvas?')
        Width = int(input('>>'))
        Height = Width
        
        print('Size of field? How many squares on one side?')
        length = input('>>')
        
        print('Enable "trimming"?')
        Trimming = input('>>')
    else:
        print('-----------------')
        print('Inmatningsfel, please try again.')
        print('-----------------')
        sys.exit()
        
    main_sheet = Field_operator.Create_random_field(length)
    Windcan = Windmodule.Windclass(Width, Height, "Simply: life")
    return main_sheet, Windcan, Trimming

main_sheet, Windcan, Trimming = U_Interface_V2()
neighbour_list = Field_operator.Initiate_blank(30)
parent = main_sheet


            
def move():
    global parent
    global main_sheet
    global neighbour_list
    global start_time
    
    Windcan.Paint_cells(main_sheet, neighbour_list) #I don't wanna paint the cells!!!
    
    if Trimming == True:
        smain_sheet, paint_list = Field_operator.Trimming(main_sheet)
        Windcan.Paint_Blood(main_sheet, paint_list)
        
    #Field_explorer.Find_ring(main_sheet, parent)
    
    parent = main_sheet
    
    end_time = time.time()
    
    if (end_time - start_time >= 10):
        start_time = time.time()
        main_sheet = Field_operator.Create_random_field(30)
    
    #Last thing -->
    main_sheet, neighbour_list = Field_operator.Tick(main_sheet, neighbour_list)
    Windcan.w_canvas.after(1, move)

move()
Windcan.root.mainloop()


'''IDEAS
1) Build another module for editing the canvas using the mouse. The module
    should have a next-button that ticks the program forwards and the program
    should show 1,2 or 3 windows of what will happen to the pattern in the
    coming generations.
2) 

'''
