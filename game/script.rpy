#counter for the char patience. will probably reset it at death and level completion. 
#other than that it'll change with interaction.
default patience_counter = 6


# The game starts here.

label start:



    scene roof_vn

    show day_0

    "You have been a detective for a while now."
    menu:
        "yeah":
            "you love your job too."
        "what no":
            "oh ok, wrong guy."
            return
    show detective with dissolve
    "This is you btw."
    menu:
        "yea":
            "A real stud."
        "no it isn't":
            "Oh. sorry."
            return
    hide detective with dissolve
    "In any case, your week is about to start"
    "Do you want to reminisce about your life before sleeping the night off?"
    menu:
        "yes":
            show detective with dissolve
            "You look up at the sky and ponder about your past..."
            "As previously mentionned, you think about how much you like your job."
            "But what your the fondest about your work isn't the sense of justice or help you bring to people."
            "It's money. Money and {b}secrets{/b}."
            "There's nothing after money that you love more than uncovering people's {b}secrets{/b}."
            "Fortunately for you, you will be visiting and interrogating suspects all week."
            "You don't"
            "Now are you ready to start your week or do you want to practice your interrogation tactics. (tutorial)"
          


        "just let me play the game":
            "See you monday!"


    jump talk_start

   
    
    return

label talk_start:

    menu:
        #those are the main choices for what topic you will talk about with the victims. they redirect to labels with actual dialogue options
        "fact checks":
            jump fact_checks
        "small talk":
            jump small_talk
        "intimidation":
            jump intimidation
        "arrest":
            jump arrest

    return

label fact_checks:
    menu:
        
        "time":
            mc "where were you yesterday at 9pm?"
            v "asleep."
            jump fact_checks
        
        "profession":
            mc "so, mr Velinicci, what's your job?"
            v "I own a petshop."
            v "I used to have a studio for it but now I do it right in here, in my house."
            jump fact_checks  
        
        "relationship":
            mc "sir did you have any form of relationship to the victim?"
            v "Never heard of the guy."
            
            menu:
                
                "have you had any other major relationship in your life":
                    v "no."
                    v "I've been alone for as long as I can remember."#gonna add sus counter or something
                    show Velinicci at left
                    show parrot at right 
                    with dissolve
                    #the with dissolve makes them seem to appear simultaneously and adding a transition automatically
                    p "..."
                    "the parrot looks sad."
                    hide parrot
                    show Velinicci at center 
                    with dissolve
                    jump fact_checks

                "He was your employee":
                    v "Was he?"
                    v "I don't think so."
                    "the owner looks at me challengingly"
                    
                    menu:
                        
                        "threaten":
                            mc "You really should think about the way youre talking to a law representative."
                            v "you're."
                            mc "what..?"
                            v "it's you're, not youre."
                            "You've never felt so humiliated."
                            "You remained silent and left the house without continuing the interrogation."
                            "You Dunce."
                            jump losing
                        
                        "state the facts":
                            mc "Sir our reports clearly state that Solomon Wonkus, the victim, worked for you since the last two months."
                            v "I'm telling you I never heard of the guy!"
                            v "As a matter of fact, I've been running this business by myself for my whole life!"
                            show Velinicci at left 
                            show parrot at right
                            with dissolve
                            p "Mr.V? Do you want me to put the boxes here?"
                            v "..."
                            p "Mr.V, I won't be able to come to work, {b}friday{/b}."
                            v "..."
                            p "Hello sir, i'd like to apply here, my name is..."
                            #play animation
                            hide parrot
                            show Velinicci at center
                            with dissolve
                            "Mr.Velinicci punched the parrot."

                            #would parrot and lose patience
                            jump fact_checks

                
                "I understand":
                    jump fact_checks



        "go back":
            jump talk_start
       
    return

label small_talk:
    return

label intimidation:
    return

label arrest:


    "are you sure?"


    menu:
        "Arrest":
            return#would probably call a function here
        "Go back":
            jump talk_start

    return

label losing:
    return