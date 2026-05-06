# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import random
    bgm_tracks = [
        "loop.wav",
        "loop2.wav"
    ]

define e = Character("Sheep")
define p = Character("You")
define s = Character("Strange Person")

$name = ""

default persistent.good_ending = False
default persistent.bad_ending = False

image house:
        "images/bg_house.png"

image forest:
        "images/bg_forest.png"

image forestDay:
        "images/bg_forest_night.png"

image city:
        "images/bg_city.png"

image store:
        "images/bg cookies.png"

default sadness = 0
default happy = 0

define w = Character("william")

label start:
        $ selected_bgm = random.choice(bgm_tracks)
        play music selected_bgm fadein 1.0 loop

        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.
        with fade
        scene house

        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.

        "You just wake up"
        "This is the start of the day"
        "You see something infront of you"

        show s_happy

        menu :
                "Approach Animal":
                        jump Sheep
                "Ignore":
                        jump ignore

label Sheep :
        show s_exited
        hide s_happy

        with fade
        e "Hello there!"
        hide s_exited

        show s_happy
        e "You're new here!"
        e "Want me to show you around?"
        e "Seems like you just woke up."

        p "Okay, I would love that."
        p "Who are you though?"
        hide s_happy

        show s_wonder
        e "Uhh..."
        e "I usually wander around here looking for food."
        e "There are some quality goods here."
        e "Anyway what's yout name?"

        $name = renpy.input(default='', prompt="Anyway what's yout name?")

        e "Hi %(name)s !"   
        hide s_wonder



        scene black
        with fade

        "Sheep takes you to wherever it is."
        "You didn't realize that he brought you to the middle of the forest."

        scene bg_forest
        with fade 

        show s_happy
        e "Hey %(name)s, are you listening?"
        e "Heyy!!!"
        hide s_happy

        show s_wonder
        p "Woah..."
        p "Sorry, I feel tired."
        hide s_wonder

        show s_happy
        e "Alright, we can take a rest."
        e "We'll continue tomorrow."
        hide s_happy

        show s_exited
        p "WAIT... so..."
        p "WE HAVEN'T EXPLORED EVERYTHING YET???"
        hide s_exited

        show s_happy
        e "Hehe, this place is..."
        e "Quite..."
        e "..."
        e "Massive..."
        hide s_happy

        scene black
        "You're too tired to answer."
        "You fall asleep right away."

        scene forestDay
        with fade 

        p "Woah..."
        p "Where is Sheep?"

        "Sheep suddenly appears out of nowhere."
        show s_happy

        e "You're awake!"
        p "Where were you going?"
        e "I was waiting for you to wake up."
        e "Hey, do you know about a round brown thing?"
        e "I saw someone eating one."

        p "Oh, you mean cookies?"
        e "What is that?"

        p "It's a food that tastes really sweet and delicious."
        hide s_happy

        show s_exited
        p "It's like eating a crunchy cloud."
        p "Really worth trying!"

        e "WOW WOW WOW, I WANT TO TRY IT!"
        e "WHERE CAN I GET THAT?"

        p "Of course, not in the middle of the forest."

        menu:
                "Will you take me to the cookies?"
                "Yes, I will":
                        jump yes
                        $ happy += 3
                "No":
                        jump no
                        $ sadness += 3

label yes:
        e "WAIT, REALLY?!"
        p "Yeah, and please let's leave this forest..."
        e "ALRIGHT, LET'S GO!"
        hide s_exited
        show black
        "you and sheep goes to the nearest city"

        show city
        with fade

        show s_happy
        e "We arrived!"
        p "Now we need to search for a cookie shop."
        e "Alright, show me the way!"
        p "..."

        menu: 
                "I don't know where the cookie store is":
                        $ sadness += 3
                        hide s_happy
                        show s_sad
                "Let's find a map!":
                        $ happy += 3
        hide s_sad
        hide s_happy
        show s_happy

        e "Okay."
        e "Then let's walk around."

        show black
        with fade
        "After 1 hour of searching..."


        e "I FOUND A MAP!"
        p "YAY, LET'S FIND THE COOKIES!"
        p "We should go this way."
        e "OKAYY!"
        
        show black
        with fade
        "After 2 hours of searching..."

        e "IS THAT IT?"
        p "THAT'S IT!"
        hide s_happy
        hide black

        scene store

        e "It's closed...."

        $ emotions = {"sad": sadness, "happy": happy}
        "You made the sheep feel really [max(emotions, key=emotions.get)]."

        if sadness >= 3:
                $ persistent.bad_ending = True
        elif happy >= 3:
                $ persistent.good_ending = True
        
        if persistent.good_ending == True:
                "{b}Cookies Happy Ending (Good){/b}."
        elif persistent.bad_ending == True:
                "{b}Cookies Sad Ending (Good){/b}."
        return

label no:
        hide s_exited
        show s_sad
        e "Okay..."
        e "What should we do then?"

        menu:
                "Just walk":
                        $ sadness += 3 
                "Uh... let's find the person you mentioned":
                        $ happy += 3
        e "Okay...."

        show black
        with fade
        "After 2 hours of searching..."
        hide black

        e "THAT'S THE PERSON!"
        hide s_sad
        show s_exited at left

        p "Hey, where did you get those cookies?"
        
        show strangeperson at right
        s "Uhh...."
        s "I bought them..."
        s "At a store, and it's really far."

        p "Show Us!"
        
        s "Apparently, the owner said they will close the store."
        hide s_exited
        show s_sad at left
        s "Because he's too old to run the business."
        s "And I was the last buyer..."
        s "...."

        show black
        with fade

        "After hearing that, you and the sheep part ways."

        $ emotions = {"sad": sadness, "happy": happy}
        "You made the sheep feel really [max(emotions, key=emotions.get)]."

        if sadness >= 6:
                $ persistent.bad_ending = True
        elif happy >= 6:
                $ persistent.good_ending = True
        
        if persistent.good_ending == True:
                "{b}REALLY REALLY BAD ENDING (but the sheep feels happy with you){/b}."
        elif persistent.bad_ending == True:
                "{b}REALLY REALLY BAD ENDING (but the sheep feels disappointed with you){/b}."
        return

label ignore :
        hide s_happy
        "you eat then sleep"
        "{b}Bad Ending{/b}."

        return
