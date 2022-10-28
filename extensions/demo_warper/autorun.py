# Based on the documentation example available at https://www.renpy.org/doc/html/atl.html#warpers
import renpy

@renpy.atl.atl_warper
def linear_ext(t):
    return t
