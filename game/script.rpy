label main_menu:
    # Skip main menu
    return

label start:
    call main_choice
    return

label main_choice:
    $ quick_menu = True
    $ renpy.block_rollback()
    $ overview_mode = False
    menu:
        "Story":
            call story
        "Library":
            $ current_extension = 'demo_warper'
            $ renpy.block_rollback()
            $ quick_menu = False
            $ overview_mode = True
            call screen file_explorer()
        "Exit":
            return
    jump main_choice

label story:
    "Oh. Hi. I guess you are here to learn about Ren'Py extensions... Give me a minute, will you?"
    "I'm happy to see new faces here."
    "Did you know that Ren'Py extensions are nearly as old as Ren'Py itself?"
    "They were added in 2007, only 2 years after Ren'Py's creation but a lack of documentation made them the exclusivity of a select few."
    "That made sense though, they were intended as a mean to patch Ren'Py itself should an issue occur, not as something game developpers should use."
    "But maybe it's time for them to realize more of the potential they have despite their humble beginnings."

    "I made some research in this direction at the time. Where did I put those documents?{w=.5}.{w=.5}.{w=.5}.{w=1} Here they are, let's take a look."
    show screen compilation_instructions()
    with dissolve
    "I remember now. I had to create my extension files by hand at the time."
    "If memory serves me right, I ended up learning how to create a script that I would always run from my extension's directory."
    "It was something like {color=#888}python -m zipfile -c ../game *{/color}."
    "At some point I even learned how to run this script using only Ren'Py, but this time is far behind me now."
    hide screen compilation_instructions
    with dissolve

    "Anyway, here are some of my old projects. I remember that they were based off the official documentation."
    "I'm going to show them to you, however keep in mind that once you start looking at code, you will have to click down here to keep progressing."

    show screen file_explorer()
    show screen demo_warper_example()
    $ current_extension = 'demo_warper'
    "Here comes the first extension, it simply defines a custom warper that we can make use of.\nClick down here to progress..."
    "You can take a look at its code by clicking the files listed on the right. First, click on {color=#888}examples/demo_warper.rpy{/color} and continue."
    "This is a simple Ren'Py file that makes use of my extension, not the extension itself."
    "It declares a new image that is displayed in the {color=#888}demo_warper_example{/color} screen. Notice how it uses a {color=#888}linear_ext{/color} warper, which does not exist in Ren'Py."
    "Now open the file {color=#888}autorun.py{/color}. This file is mandatory in all Ren'Py extensions and is the one that is executed by Ren'Py when it loads the extension."
    "The first thing I did here is load renpy, as it is not available by default in an extension."
    "Then, I simply created the warper as the documentation recommends.{w=1} With one exception. Can you spot it?"
    "I changed the way I access the {color=#888}atl_warper{/color} decorator. In a rpy file, I would write {color=#888}@renpy.atl_warper{/color}, but it doesn't work the same way in extensions."
    "What is important in an extension is the way Ren'Py organizes its content, not the way it shows it when you are in a rpy file."
    "Il you want to use the same layout as from rpy files, you need to prepend the resource you want with {color=#888}renpy.store{/color}."
    "In this specific, you would need to write {color=#888}@renpy.store.renpy.atl_warper{/color}. I do not recommend you do, but it does work."
    "Got it? Let's take a look at another extension that I wrote a bit later."
    hide screen demo_warper_example
    with dissolve

    $ current_extension = 'demo_label_random'
    "This extension is a bit quirky, it randomly chooses a text option among many and only prints that one out. Look at {color=#888}examples/demo_label_random.rpy{/color} to see how to use it."
    "Now open {color=#888}autorun.py{/color}. Do you see the {color=#888}from demo_random_label{/color} statement?"
    "It imports the content of the file {color=#888}demo_label_random.py{/color} and registers the statement I use in {color=#888}examples/demo_label_random.rpy{/color} into Ren'Py."
    "Just like {color=#888}demo_label_random{/color}, any module can be made available to rpy files once it is declared in an extension file."
    "Keep in mind that any change you make to Ren'Py MUST be performed in your autorun, otherwise it might be lost and crash your game when reloading the game during developement."
    "Let's summon the example for this extension once, you can rollback and go forward again to see all potential texts, and then we will go over to a different example."
    call demo_label_random

    show screen demo_appearing_example()
    $ current_extension = 'demo_appearing'

    "This extension is a bit shy, move your cursor around the center of the screen to see what it does."
    "It can be used in different ways, take a look at {color=#888}examples/demo_appearing.rpy{/color}, I created two screens that show the same thing but used my {color=#888}Appearing{/color} extension in different ways."
    "The second one directly uses the Displayable's class, while the first one uses a custom screen label."
    "Could you open {color=#888}autorun.py{/color} so that I could tell you how I achieved this ?"
    "Again, I created a module ({color=#888}demo_appearing{/color}) to store my Displayable, however if I did nothing I would have needed to import the module each time I wanted to use it."
    "To avoid this, I added my Displayable to the store. Do you see the line starting with {color=#888}renpy.store{/color}? That's how you do it with static data."
    "To add my Displayable to the screen Parser, I had to do a bit more. Everything else in the {color=#888}autorun.py{/color} is necessary to add it."
    "If you're curious, look at the comments I wrote at the time, my memory is pretty hazy."
    hide screen demo_appearing_example
    hide screen file_explorer
    with dissolve

    "That's about it for the basics, if you want to look at all the extensions I have on hand right now, you might want to take a look at my library"
    "I have put the extension I used to add colors to the files I showed you there, though you will have to understand its content on your own."
    "If you do look it up, stay far from the {color=#888}pygment{/color} directory, it is a module I didn't develop and is beyond the scope of this demo."

    return
