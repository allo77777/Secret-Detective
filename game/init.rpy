init:
    $day_arr = ["day_0_v2", "day_1_v2", "day_2_v2", "day_3_v2", "day_4_v2", "day_5_v2",]
    $day_counter = 1
    $dialogue_choice = "adad"

#this func is for called when pressed on the talk option screen. its a if statement to redirect to the dialogue matching the day counter
    #def day_dialogue():
        #if day_counter == 1: 
            #jump f"{dialogue_choice}_{day_counter}" 
init python:
    def day_dialogue():
        if day_counter == 1: 
            renpy.jump(day_label)