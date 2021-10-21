from tkinter import *
import tkinter
from tkinter import Canvas
import datetime
from PIL import Image,ImageTk
import random #to pick between player
import time # for dramatic delays

#p1 == player
#p2 == cpu
random_pick = random.choice(["p2","p1"])

player_turn_list = [random_pick] #to know whose turn it is
# player_turn_list = ["p1"] #to know whose turn it is....starting with player for now

Game_status = ["playing"] #is it won or not
box_val = {} # to store value for individual boxes. x o x o
for digit in range (1,17):
    box_name = "pid" + str(digit)
    box_val[box_name] = {} #creates blank keys for all boxes
    box_val[box_name]["value"]="blank"

def ui_elements():
    window = Tk() #creating the main window of an app
    window.iconphoto(False, tkinter.PhotoImage(file='joystick.png'))
    window.title(" ")
    window.geometry("760x450")
    window.configure(bg = "#ffffff")

    canvas1 = Canvas(
        window,
        bg = "#ffffff",
        height = 450,
        width = 760,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas1.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"bg.png")
    canvas1.create_image(380.0, 225.0,image=background_img)

    #game objects(images)
    pick0= ImageTk.PhotoImage(Image.open('blank.png').resize((60,60))) #game start
    pick2= ImageTk.PhotoImage(Image.open('xo.png').resize((65,65))) #letter "o"
    pick1= ImageTk.PhotoImage(Image.open('ox.png').resize((60,60))) #letter "x"
    
#************************************** GAME ENGINE *******************************************#    

    def Game_Engine():
        # pass
        try:
            if player_turn_list[0] != "won":
                #row wins
                if box_val["pid1"]["value"] == "x" and box_val["pid2"]["value"] == "x" and box_val["pid3"]["value"] == "x" \
                and box_val["pid4"]["value"] == "x":
                    Label(window, text="Row One Has won").place(x=125,y=150)
                    canvas1.create_line(395, 90, 650, 90, width=10)
                    Game_status[0] = "won"
                elif box_val["pid5"]["value"] == "x" and box_val["pid6"]["value"] == "x" and box_val["pid7"]["value"] == "x" \
                and box_val["pid8"]["value"] == "x":
                    Label(window, text="Row Two Has won").place(x=125,y=150)
                    canvas1.create_line(395, 175, 650, 175, width=10)
                    Game_status[0] = "won"
                elif box_val["pid9"]["value"] == "x" and box_val["pid10"]["value"] == "x" and box_val["pid11"]["value"] == "x" \
                and box_val["pid12"]["value"] == "x":
                    Label(window, text="Row Three Has won").place(x=125,y=150)
                    canvas1.create_line(395, 260, 650, 260, width=10) 
                    Game_status[0] = "won"
                elif box_val["pid13"]["value"] == "x" and box_val["pid14"]["value"] == "x" and box_val["pid15"]["value"] == "x" \
                and box_val["pid16"]["value"] == "x":
                    Label(window, text="Row Four Has won").place(x=125,y=150)
                    canvas1.create_line(395, 345, 650, 345, width=10)
                    Game_status[0] = "won"


                #column wins
                elif box_val["pid1"]["value"] == "x" and box_val["pid5"]["value"] == "x" and box_val["pid9"]["value"] == "x" \
                and box_val["pid13"]["value"] == "x":
                    Label(window, text="Column One Has won").place(x=125,y=150)
                    Game_status[0] = "won"
                elif box_val["pid2"]["value"] == "x" and box_val["pid6"]["value"] == "x" and box_val["pid10"]["value"] == "x" \
                and box_val["pid14"]["value"] == "x":
                    Label(window, text="Column Two Has won").place(x=125,y=150)
                    Game_status[0] = "won"
                elif box_val["pid3"]["value"] == "x" and box_val["pid7"]["value"] == "x" and box_val["pid11"]["value"] == "x" \
                and box_val["pid15"]["value"] == "x":
                    Label(window, text="Column Three Has won").place(x=125,y=150)
                    Game_status[0] = "won"
                elif box_val["pid4"]["value"] == "x" and box_val["pid8"]["value"] == "x" and box_val["pid12"]["value"] == "x" \
                and box_val["pid16"]["value"] == "x":
                    Label(window, text="Column Four Has won").place(x=125,y=150)
                    Game_status[0] = "won"

                #Diagonal wins
                elif box_val["pid1"]["value"] == "x" and box_val["pid6"]["value"] == "x" and box_val["pid11"]["value"] == "x" \
                and box_val["pid16"]["value"] == "x":
                    Label(window, text="Diagonal One Has won").place(x=125,y=150)
                    Game_status[0] = "won" 
                elif box_val["pid4"]["value"] == "x" and box_val["pid7"]["value"] == "x" and box_val["pid10"]["value"] == "x" \
                and box_val["pid13"]["value"] == "x":
                    Label(window, text="Diagonal Two Has won").place(x=125,y=150) 
                    Game_status[0] = "won"
        except:
            print("that thing occured")

#************************************** XO FILLER *******************************************#    

    def ive_been_clicked(pids):
        Label(window, text=pids).place(x=95,y=100)

        if pids == "refresh":
            pid1.config(image=pick0),pid2.config(image=pick0),pid3.config(image=pick0),pid4.config(image=pick0),
            pid5.config(image=pick0),pid6.config(image=pick0),pid7.config(image=pick0),pid8.config(image=pick0)
            pid9.config(image=pick0),pid10.config(image=pick0),pid11.config(image=pick0),pid12.config(image=pick0)
            pid13.config(image=pick0),pid14.config(image=pick0),pid15.config(image=pick0),pid16.config(image=pick0)

            #reset status
            Game_status[0] = "playing"

            #reset player turn
            player_turn_list.clear()
            random_refresh_pick = random.choice(["p2","p1"])
            player_turn_list.append(random_refresh_pick)

            if random_refresh_pick == "p1":  #call desired function
                human_play()
            elif random_refresh_pick == "p2": 
                cpu_random_play()

            # box_val.clear()   
            for item in box_val:
                box_val[item]["value"] = "blank"

        sectors = ["pid1","pid2","pid3","pid","pid5","pid6","pid7","pid8","pid9","pid10","pid11","pid12","pid13","pid14","pid15","pid16"]
        for box in sectors:
             #to check if box already has input
            if pids == box:
                print(f"sector: {box}")

                if player_turn_list[len(player_turn_list)-1] == "p1": #pick the last item in the list
                    player_turn_list.append("p2") #switch to the next player

                    if box == "pid1" and box_val["pid1"]["value"]=="blank":#current player ops
                        pid1.config(image=pick1)
                    elif box == "pid2" and box_val["pid2"]["value"]=="blank":
                        pid2.config(image=pick1)
                    elif box == "pid3" and box_val["pid3"]["value"]=="blank":
                        pid3.config(image=pick1)
                    elif box == "pid4" and box_val["pid4"]["value"]=="blank":
                        pid4.config(image=pick1)
                    elif box == "pid5" and box_val["pid5"]["value"]=="blank":
                        pid5.config(image=pick1)
                    elif box == "pid6" and box_val["pid6"]["value"]=="blank":
                        pid6.config(image=pick1)
                    elif box == "pid7" and box_val["pid7"]["value"]=="blank":
                        pid7.config(image=pick1)
                    elif box == "pid8" and box_val["pid8"]["value"]=="blank":
                        pid8.config(image=pick1)
                    elif box == "pid9" and box_val["pid9"]["value"]=="blank":
                        pid9.config(image=pick1)
                    elif box == "pid10" and box_val["pid10"]["value"]=="blank":
                        pid10.config(image=pick1)
                    elif box == "pid11" and box_val["pid11"]["value"]=="blank":
                        pid11.config(image=pick1)
                    elif box == "pid12" and box_val["pid12"]["value"]=="blank":
                        pid12.config(image=pick1)
                    elif box == "pid13" and box_val["pid13"]["value"]=="blank":
                        pid13.config(image=pick1)
                    elif box == "pid14" and box_val["pid14"]["value"]=="blank":
                        pid14.config(image=pick1)
                    elif box == "pid15" and box_val["pid15"]["value"]=="blank":
                        pid15.config(image=pick1)
                    elif box == "pid16" and box_val["pid16"]["value"]=="blank":
                        pid16.config(image=pick1)

                    #check if box chosen is empty, then fill
                    box_val[box]["value"]="x" #set new value for that box

        #* if we have cpu playing  
        #       time 
                    # time.sleep(1)
                    cpu_move = "now"
                if cpu_move == "now":
                    # time.sleep(1) 
                    cpu_random_play()
                    
        #* if we have a second player
                # elif player_turn_list[len(player_turn_list)-1] == "p2" : #pick the last item in the list
                #     player_turn_list.append("p1")#switch to the next player
                #     box_val[pids]["value"]="o"

                #     if box == "pid1":#current player ops
                #         pid1.config(image=pick2)
                #     elif box == "pid2":
                #         pid2.config(image=pick2)
                #     elif box == "pid3":
                #         pid3.config(image=pick2)
                #     elif box == "pid4":
                #         pid4.config(image=pick2)
                #     elif box == "pid5":
                #         pid5.config(image=pick2)
                #     elif box == "pid6":
                #         pid6.config(image=pick2)
                #     elif box == "pid7":
                #         pid7.config(image=pick2)
                #     elif box == "pid8":
                #         pid8.config(image=pick2)
                #     elif box == "pid9":
                #         pid9.config(image=pick2)
                #     elif box == "pid10":
                #         pid10.config(image=pick2)
                #     elif box == "pid11":
                #         pid11.config(image=pick2)
                #     elif box == "pid12":
                #         pid12.config(image=pick2)
                #     elif box == "pid13":
                #         pid13.config(image=pick2)
                #     elif box == "pid14":
                #         pid14.config(image=pick2)
                #     elif box == "pid15":
                #         pid15.config(image=pick2)
                #     elif box == "pid16":
                #         pid16.config(image=pick2)

                pids = None #reset the box sector

        
        # print(f"Current player: {player_turn_list[len(player_turn_list)-2]}")
        print(f"Next player: {player_turn_list[len(player_turn_list)-1]}")
        print(f"player_list: {player_turn_list}")
        print(f"game_status: {Game_status}")
        # print(f"boxes: {box_val.keys()}")
        print(f"box_values: {box_val.values()}")

        #call engine
        Game_Engine()
    


#************************************** GAME UI *******************************************#    
    

    #row +85, col +85
    #* default layout
    pid1 = Button(window,image=pick0,borderwidth=0)
    pid1.place(x=385,y=60)
    pid2 = Button(window,image=pick0,borderwidth=0)
    pid2.place(x=470,y=60)
    pid3 = Button(window,image=pick0,borderwidth=0)
    pid3.place(x=555,y=60)
    pid4 = Button(window,image=pick0,borderwidth=0)
    pid4.place(x=640,y=60)
    ##*********************************************##
    pid5 = Button(window,image=pick0,borderwidth=0)
    pid5.place(x=385,y=145)
    pid6 = Button(window,image=pick0,borderwidth=0)
    pid6.place(x=470,y=145)
    pid7 = Button(window,image=pick0,borderwidth=0)
    pid7.place(x=555,y=145)
    pid8 = Button(window,image=pick0,borderwidth=0)
    pid8.place(x=640,y=145)
    ##*********************************************##
    pid9 = Button(window,image=pick0,borderwidth=0)
    pid9.place(x=385,y=230)
    pid10 = Button(window,image=pick0,borderwidth=0)
    pid10.place(x=470,y=230)
    pid11 = Button(window,image=pick0,borderwidth=0)
    pid11.place(x=555,y=230)
    pid12 = Button(window,image=pick0,borderwidth=0)
    pid12.place(x=640,y=230)
    ##*********************************************##
    pid13 = Button(window,image=pick0,borderwidth=0)
    pid13.place(x=385,y=315)
    pid14 = Button(window,image=pick0,borderwidth=0)
    pid14.place(x=470,y=315)
    pid15 = Button(window,image=pick0,borderwidth=0)
    pid15.place(x=555,y=315)
    pid16 = Button(window,image=pick0,borderwidth=0)
    pid16.place(x=640,y=315)
    ##*********************************************##
    Refresh = Button(window,text="Refresh",borderwidth=2,cursor="dotbox",command=lambda: ive_been_clicked(pids="refresh"))
    Refresh.place(x=650,y=405)

    #* player play
    def human_play():
        pid1.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid1"))
        pid2.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid2"))
        pid3.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid3"))
        pid4.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid4"))
        ##**************************************************************************##
        pid5.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid5"))
        pid6.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid6"))
        pid7.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid7"))
        pid8.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid8"))
        ##**************************************************************************##
        pid9.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid9"))
        pid10.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid10"))
        pid11.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid11"))
        pid12.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid12"))
        ##**************************************************************************##
        pid13.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid13"))
        pid14.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid14"))
        pid15.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid15"))
        pid16.config(cursor="dotbox",command=lambda: ive_been_clicked(pids="pid16"))
        ##**************************************************************************##
        
    def cpu_random_play():
        time.sleep(0.2)    #thinking time 
        cpu_choice = random.choice(["pid1","pid2","pid3","pid4","pid5","pid6","pid7","pid8","pid9","pid10","pid11","pid12","pid13","pid14","pid15","pid16"])
        player_turn_list.append("p1")#switch to the next player
        
        while box_val[cpu_choice]["value"] !="blank": #if already occupied, pick another box
            cpu_choice = random.choice(["pid1","pid2","pid3","pid4","pid5","pid6","pid7","pid8","pid9","pid10","pid11","pid12","pid13","pid14","pid15","pid16"])

        if cpu_choice == "pid1":#current player ops
            pid1.config(image=pick2)   
        elif cpu_choice == "pid2":
            pid2.config(image=pick2)
        elif cpu_choice == "pid3":
            pid3.config(image=pick2)
        elif cpu_choice == "pid4":
            pid4.config(image=pick2)
        elif cpu_choice == "pid5":
            pid5.config(image=pick2)
        elif cpu_choice == "pid6":
            pid6.config(image=pick2)
        elif cpu_choice == "pid7":
            pid7.config(image=pick2)
        elif cpu_choice == "pid8":
            pid8.config(image=pick2)
        elif cpu_choice == "pid9":
            pid9.config(image=pick2)
        elif cpu_choice == "pid10":
            pid10.config(image=pick2)
        elif cpu_choice == "pid11":
            pid11.config(image=pick2)
        elif cpu_choice == "pid12":
            pid12.config(image=pick2)
        elif cpu_choice == "pid13":
            pid13.config(image=pick2)
        elif cpu_choice == "pid14":
            pid14.config(image=pick2)
        elif cpu_choice == "pid15":
            pid15.config(image=pick2)
        elif cpu_choice == "pid16":
            pid16.config(image=pick2)

            
        #check if box chosen is empty, then fill
        box_val[cpu_choice]["value"]="o" #set new value for that box
        
        # print(f"Current player: {player_turn_list[len(player_turn_list)-2]}")
        print(f"Next player: {player_turn_list[len(player_turn_list)-1]}")
        print(f"player_list: {player_turn_list}")
        print(f"game_status: {Game_status}")
        # print(f"boxes: {box_val.keys()}")
        print(f"box_values: {box_val.values()}")

        #call engine
        Game_Engine()

        #* if we have human playing next 
        human_play()
        cpu_choice = None
#************************************** GAME UI *******************************************# 


    #* cpu guess
    if random_pick == "p1": 
        human_play()
    elif random_pick == "p2": 
        cpu_random_play()
    
    # if player_turn_list[len(player_turn_list)-1] == "p1": #pick the last item in the list
    #     human_play()

    # elif player_turn_list[len(player_turn_list)-1] == "p2":
    #     cpu_random_play()

        
        

    #clock timer       
    def clock():
        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        if int(hour) > 12 and int(hour) < 24:
                time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        time_label.config(text = time)
        # date_label.config(text= date)
        time_label.after(1000, clock)

    time_label = Label(canvas1, font = 'Helvetica 13 bold', foreground = 'black')
    time_label.place(x=65,y=335)

    clock()

    window.resizable(False, False)
    # opacity/tranparency applies to image and frame
    # window.wm_attributes('-alpha', 0.95)  
    window.mainloop()

    

def tic_elements(window):
        new_frame = Frame(window,bg="red")
        new_frame.place(x=365,y=50)




if __name__=="__main__":
    #close contents into functions
    ui_elements()
    
    