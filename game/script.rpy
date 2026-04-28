# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Sheep")

image house:
        "images/bg_house.png"

image shappy:
        "images/s_happy.png"


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
    with fade
    show s_exited

    e "Hello there!"
    hide s_exited

    show s_happy
    e "Good day, What's your name?"
    return

label ignore :
    hide s_happy
    "you eat then sleep"
    "{b}Bad Ending{/b}."
    # This ends the game.

    return
