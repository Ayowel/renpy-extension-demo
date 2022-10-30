# This is based on the documentation example available at
# https://www.renpy.org/doc/html/atl.html#warpers
import renpy

# Note how we have to use
# @renpy.atl.atl_warper instead of @renpy.atl_warper
# as we have to use the real path of the module instead
# of relying on the store-based layout.
@renpy.atl.atl_warper
def linear_ext(t):
    return t
