# This is based on the documentation example available at
# https://www.renpy.org/doc/html/cdd.html
import renpy
from demo_appearing import Appearing

#####
# Add Appearing to the Ren'Py Store.
# If this is not set, explicit instanciation of the class
# requires to import the spirited module
#####
renpy.store.__dict__.setdefault('Appearing', Appearing)

#####
# Add Appearing to screen language v2.
# Adding compatibility for screen language v1 requires similar steps
# but with the renpy.screenlang module instead of renpy.sl2 submodules
#####
# Create the parser object and register its parameters
appearing_parser = renpy.sl2.sldisplayables.DisplayableParser("appearing", Appearing, "default", 0)
# Register all valid parameters
renpy.sl2.sldisplayables.Positional("child")
for keyword in [ 'opaque_distance', 'transparent_distance' ]:
    renpy.sl2.sldisplayables.Keyword(keyword)
renpy.sl2.sldisplayables.add(renpy.sl2.slproperties.position_properties)

# Add as valid child for all screen containers
# The list of all parsers is saved in renpy.sl2.slparser.all_statements
for i in renpy.sl2.slparser.childbearing_statements:
    i.add(appearing_parser)
# Add as valid child for screens
renpy.sl2.slparser.screen_parser.add(appearing_parser)

# Cleanup after registering the parser
renpy.sl2.slparser.parser = None
