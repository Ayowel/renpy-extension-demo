﻿# The script of the game goes in this file.

label start:

    # These display lines of dialogue.

    show screen demo_appearing_example

    "A hidden appearing image, move your cursor around the center of the screen"

    hide screen demo_appearing_example
    show screen demo_appearing_example_class

    "The same image, but in the screen's code we use a class instanciation !"

    hide screen demo_appearing_example_class
    return
