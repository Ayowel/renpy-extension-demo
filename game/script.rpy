# The script of the game goes in this file.

label start:

    # These display lines of dialogue.

    show screen demo_appearing_example

    "A hidden appearing image, move your cursor around the center of the screen"

    hide screen demo_appearing_example
    show screen demo_appearing_example_class

    "The same image, but in the screen's code we use a class instanciation !"

    hide screen demo_appearing_example_class
    show screen demo_warper_example

    "A moving image with a custom warper"

    hide screen demo_warper_example

    "A random lorem ipsum word is coming up, rollback to see them all !"
    random:
        "Lorem."
        "Ipsum"
        "Dolor"
        "Sic"
        "Amet"

    return
