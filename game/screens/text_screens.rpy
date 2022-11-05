screen compilation_instructions():
    style_prefix 'compilation_instructions'
    text _("How to create and use an extension?"):
        xalign 0.5 yalign 0.05
        size 60
    vbox:
        xalign 0.5 yalign 0.5
        text _("1 - Create a directory for your extension.")
        text _("2 - Create a file {color=#f00}autorun.py{/color} in your directory.")
        text _("3 - Add all the files in the directory to a {color=#f00}ZIP archive{/color}.")
        text _("4 - Change the extension of the archive to '{color=#f00}.rpe{/color}'.")
        text _("5 - Move the archive to the '{color=#f00}game{/color}' directory of your game.")
        text ""
        text _("You're done!")
        text _("This extension won't do much, but it's yours!")

style compilation_instructions_text:
    text_align 0.5
    xalign 0.5
