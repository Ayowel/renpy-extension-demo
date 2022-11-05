# TODO: Translation updated at 2022-11-05 20:01

# game/script.rpy:23
translate en_US story_463014ee:

    # "Oh. Hi. I guess you are here to learn about Ren'Py extensions... Give me a minute, will you?"
    "Oh. Hi. I guess you are here to learn about Ren'Py extensions... Give me a minute, will you?"

# game/script.rpy:24
translate en_US story_aae17319:

    # "I'm happy to see new faces here."
    "I'm happy to see new faces here."

# game/script.rpy:25
translate en_US story_3e3b3dff:

    # "Did you know that Ren'Py extensions are nearly as old as Ren'Py itself?"
    "Did you know that Ren'Py extensions are nearly as old as Ren'Py itself?"

# game/script.rpy:26
translate en_US story_fd4a6de1:

    # "They were added in 2007, only 2 years after Ren'Py's creation but a lack of documentation made them the exclusivity of a select few."
    "They were added in 2007, only 2 years after Ren'Py's creation but a lack of documentation made them the exclusivity of a select few."

# game/script.rpy:27
translate en_US story_1b609d08:

    # "That made sense though, they were intended as a mean to patch Ren'Py itself should an issue occur, not as something game developpers should use."
    "That made sense though, they were intended as a mean to patch Ren'Py itself should an issue occur, not as something game developpers should use."

# game/script.rpy:28
translate en_US story_b78d1082:

    # "But maybe it's time for them to realize more of the potential they have despite their humble beginnings."
    "But maybe it's time for them to realize more of the potential they have despite their humble beginnings."

# game/script.rpy:30
translate en_US story_3a5720da:

    # "I made some research in this direction at the time. Where did I put those documents?{w=.5}.{w=.5}.{w=.5}.{w=1} Here they are, let's take a look."
    "I made some research in this direction at the time. Where did I put those documents?{w=.5}.{w=.5}.{w=.5}.{w=1} Here they are, let's take a look."

# game/script.rpy:33
translate en_US story_adf41934:

    # "I remember now. I had to create my extension files by hand at the time."
    "I remember now. I had to create my extension files by hand at the time."

# game/script.rpy:34
translate en_US story_5ce9412e:

    # "If memory serves me right, I ended up learning how to create a script that I would always run from my extension's directory."
    "If memory serves me right, I ended up learning how to create a script that I would always run from my extension's directory."

# game/script.rpy:35
translate en_US story_f5e117cc:

    # "It was something like {color=#888}python -m zipfile -c ../game *{/color}."
    "It was something like {color=#888}python -m zipfile -c ../game *{/color}."

# game/script.rpy:36
translate en_US story_171df051:

    # "At some point I even learned how to run this script using only Ren'Py, but this time is far behind me now."
    "At some point I even learned how to run this script using only Ren'Py, but this time is far behind me now."

# game/script.rpy:40
translate en_US story_a33f833e:

    # "Anyway, here are some of my old projects. I remember that they were based off the official documentation."
    "Anyway, here are some of my old projects. I remember that they were based off the official documentation."

# game/script.rpy:41
translate en_US story_57c64c2c:

    # "I'm going to show them to you, however keep in mind that once you start looking at code, you will have to click down here to keep progressing."
    "I'm going to show them to you, however keep in mind that once you start looking at code, you will have to click down here to keep progressing."

# game/script.rpy:46
translate en_US story_1cc14f85:

    # "Here comes the first extension, it simply defines a custom warper that we can make use of.\nClick down here to progress..."
    "Here comes the first extension, it simply defines a custom warper that we can make use of.\nClick down here to progress..."

# game/script.rpy:47
translate en_US story_f2b51c96:

    # "You can take a look at its code by clicking the files listed on the right. First, click on {color=#888}examples/demo_warper.rpy{/color} and continue."
    "You can take a look at its code by clicking the files listed on the right. First, click on {color=#888}examples/demo_warper.rpy{/color} and continue."

# game/script.rpy:48
translate en_US story_0648a007:

    # "This is a simple Ren'Py file that makes use of my extension, not the extension itself."
    "This is a simple Ren'Py file that makes use of my extension, not the extension itself."

# game/script.rpy:49
translate en_US story_ead830c2:

    # "It declares a new image that is displayed in the {color=#888}demo_warper_example{/color} screen. Notice how it uses a {color=#888}linear_ext{/color} warper, which does not exist in Ren'Py."
    "It declares a new image that is displayed in the {color=#888}demo_warper_example{/color} screen. Notice how it uses a {color=#888}linear_ext{/color} warper, which does not exist in Ren'Py."

# game/script.rpy:50
translate en_US story_d39020f8:

    # "Now open the file {color=#888}autorun.py{/color}. This file is mandatory in all Ren'Py extensions and is the one that is executed by Ren'Py when it loads the extension."
    "Now open the file {color=#888}autorun.py{/color}. This file is mandatory in all Ren'Py extensions and is the one that is executed by Ren'Py when it loads the extension."

# game/script.rpy:51
translate en_US story_bb531d9a:

    # "The first thing I did here is load renpy, as it is not available by default in an extension."
    "The first thing I did here is load renpy, as it is not available by default in an extension."

# game/script.rpy:52
translate en_US story_4fc1b6c1:

    # "Then, I simply created the warper as the documentation recommends.{w=1} With one exception. Can you spot it?"
    "Then, I simply created the warper as the documentation recommends.{w=1} With one exception. Can you spot it?"

# game/script.rpy:53
translate en_US story_29783a6e:

    # "I changed the way I access the {color=#888}atl_warper{/color} decorator. In a rpy file, I would write {color=#888}@renpy.atl_warper{/color}, but it doesn't work the same way in extensions."
    "I changed the way I access the {color=#888}atl_warper{/color} decorator. In a rpy file, I would write {color=#888}@renpy.atl_warper{/color}, but it doesn't work the same way in extensions."

# game/script.rpy:54
translate en_US story_a924a200:

    # "What is important in an extension is the way Ren'Py organizes its content, not the way it shows it when you are in a rpy file."
    "What is important in an extension is the way Ren'Py organizes its content, not the way it shows it when you are in a rpy file."

# game/script.rpy:55
translate en_US story_b3e0c31e:

    # "Il you want to use the same layout as from rpy files, you need to prepend the resource you want with {color=#888}renpy.store{/color}."
    "Il you want to use the same layout as from rpy files, you need to prepend the resource you want with {color=#888}renpy.store{/color}."

# game/script.rpy:56
translate en_US story_dde6d455:

    # "In this specific, you would need to write {color=#888}@renpy.store.renpy.atl_warper{/color}. I do not recommend you do, but it does work."
    "In this specific, you would need to write {color=#888}@renpy.store.renpy.atl_warper{/color}. I do not recommend you do, but it does work."

# game/script.rpy:57
translate en_US story_d86e2718:

    # "Got it? Let's take a look at another extension that I wrote a bit later."
    "Got it? Let's take a look at another extension that I wrote a bit later."

# game/script.rpy:62
translate en_US story_04f177db:

    # "This extension is a bit quirky, it randomly chooses a text option among many and only prints that one out. Look at {color=#888}examples/demo_label_random.rpy{/color} to see how to use it."
    "This extension is a bit quirky, it randomly chooses a text option among many and only prints that one out. Look at {color=#888}examples/demo_label_random.rpy{/color} to see how to use it."

# game/script.rpy:63
translate en_US story_8d95176d:

    # "Now open {color=#888}autorun.py{/color}. Do you see the {color=#888}from demo_random_label{/color} statement?"
    "Now open {color=#888}autorun.py{/color}. Do you see the {color=#888}from demo_random_label{/color} statement?"

# game/script.rpy:64
translate en_US story_42041b05:

    # "It imports the content of the file {color=#888}demo_label_random.py{/color} and registers the statement I use in {color=#888}examples/demo_label_random.rpy{/color} into Ren'Py."
    "It imports the content of the file {color=#888}demo_label_random.py{/color} and registers the statement I use in {color=#888}examples/demo_label_random.rpy{/color} into Ren'Py."

# game/script.rpy:65
translate en_US story_e93c2f6f:

    # "Just like {color=#888}demo_label_random{/color}, any module can be made available to rpy files once it is declared in an extension file."
    "Just like {color=#888}demo_label_random{/color}, any module can be made available to rpy files once it is declared in an extension file."

# game/script.rpy:66
translate en_US story_753bdc66:

    # "Keep in mind that any change you make to Ren'Py MUST be performed in your autorun, otherwise it might be lost and crash your game when reloading the game during developement."
    "Keep in mind that any change you make to Ren'Py MUST be performed in your autorun, otherwise it might be lost and crash your game when reloading the game during developement."

# game/script.rpy:67
translate en_US story_d61a6ab2:

    # "Let's summon the example for this extension once, you can rollback and go forward again to see all potential texts, and then we will go over to a different example."
    "Let's summon the example for this extension once, you can rollback and go forward again to see all potential texts, and then we will go over to a different example."

# game/script.rpy:73
translate en_US story_f07b0019:

    # "This extension is a bit shy, move your cursor around the center of the screen to see what it does."
    "This extension is a bit shy, move your cursor around the center of the screen to see what it does."

# game/script.rpy:74
translate en_US story_fae84070:

    # "It can be used in different ways, take a look at {color=#888}examples/demo_appearing.rpy{/color}, I created two screens that show the same thing but used my {color=#888}Appearing{/color} extension in different ways."
    "It can be used in different ways, take a look at {color=#888}examples/demo_appearing.rpy{/color}, I created two screens that show the same thing but used my {color=#888}Appearing{/color} extension in different ways."

# game/script.rpy:75
translate en_US story_5aefa4d5:

    # "The second one directly uses the Displayable's class, while the first one uses a custom screen label."
    "The second one directly uses the Displayable's class, while the first one uses a custom screen label."

# game/script.rpy:76
translate en_US story_a4d8d432:

    # "Could you open {color=#888}autorun.py{/color} so that I could tell you how I achieved this ?"
    "Could you open {color=#888}autorun.py{/color} so that I could tell you how I achieved this ?"

# game/script.rpy:77
translate en_US story_ae4ed876:

    # "Again, I created a module ({color=#888}demo_appearing{/color}) to store my Displayable, however if I did nothing I would have needed to import the module each time I wanted to use it."
    "Again, I created a module ({color=#888}demo_appearing{/color}) to store my Displayable, however if I did nothing I would have needed to import the module each time I wanted to use it."

# game/script.rpy:78
translate en_US story_909652b6:

    # "To avoid this, I added my Displayable to the store. Do you see the line starting with {color=#888}renpy.store{/color}? That's how you do it with static data."
    "To avoid this, I added my Displayable to the store. Do you see the line starting with {color=#888}renpy.store{/color}? That's how you do it with static data."

# game/script.rpy:79
translate en_US story_9c9ce3d3:

    # "To add my Displayable to the screen Parser, I had to do a bit more. Everything else in the {color=#888}autorun.py{/color} is necessary to add it."
    "To add my Displayable to the screen Parser, I had to do a bit more. Everything else in the {color=#888}autorun.py{/color} is necessary to add it."

# game/script.rpy:80
translate en_US story_e4845af2:

    # "If you're curious, look at the comments I wrote at the time, my memory is pretty hazy."
    "If you're curious, look at the comments I wrote at the time, my memory is pretty hazy."

# game/script.rpy:85
translate en_US story_1bb03b6a:

    # "That's about it for the basics, if you want to look at all the extensions I have on hand right now, you might want to take a look at my library"
    "That's about it for the basics, if you want to look at all the extensions I have on hand right now, you might want to take a look at my library"

# game/script.rpy:86
translate en_US story_732b83d4:

    # "I have put the extension I used to add colors to the files I showed you there, though you will have to understand its content on your own."
    "I have put the extension I used to add colors to the files I showed you there, though you will have to understand its content on your own."

# game/script.rpy:87
translate en_US story_0cbe63f3:

    # "If you do look it up, stay far from the {color=#888}pygment{/color} directory, it is a module I didn't develop and is beyond the scope of this demo."
    "If you do look it up, stay far from the {color=#888}pygment{/color} directory, it is a module I didn't develop and is beyond the scope of this demo."

translate en_US strings:

    # game/script.rpy:9
    old "Story"
    new "Story"

    # game/script.rpy:9
    old "Library"
    new "Library"

    # game/script.rpy:9
    old "Exit"
    new "Exit"

