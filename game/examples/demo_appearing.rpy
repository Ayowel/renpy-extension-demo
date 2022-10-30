# Use a custom screen label to instanciate the 'appearing' extension's Displayable
screen demo_appearing_example():
    appearing "gui/window_icon.png":
        opaque_distance 100
        transparent_distance 200
        xalign 0.5
        yalign 0.5

# Use an explicit class reference to instanciate the 'appearing' extension's Displayable
screen demo_appearing_example_class():
    add Appearing("gui/window_icon.png", 100, 200):
        xalign 0.5
        yalign 0.5
