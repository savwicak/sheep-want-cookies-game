# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Sheep")
define p = Character("Me")

image house:
        "images/bg_house.png"

image forest:
        "images/bg_forest.png"

image forestDay:
        "images/bg_forest_night.png"


label start:

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
    hide s_wonder

    scene black
    with fade

    "Sheep takes you to wherever it is."
    "You didn't realize that he brought you to the middle of the forest."

    scene bg_forest
    with fade 

    show s_happy
    e "Hey, are you listening?"
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
        "No":
            jump no

label yes:
    e "WAIT, REALLY?!"
    p "Yeah, and please let's leave this forest..."
    e "ALRIGHT, LET'S GO!"

    "{b}Cookies Ending (Good){/b}."
    return

label no:
    hide s_exited
    show s_sad
    e "Okay..."

    "{b}REALLY REALLY BAD ENDING{/b}."
    return

label ignore :
    hide s_happy
    "you eat then sleep"
    "{b}Bad Ending{/b}."
    # This ends the game.

    return
