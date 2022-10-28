# This is based on the documentation example available at https://www.renpy.org/doc/html/cdd.html
import renpy
from demo_appearing import Appearing

# Add Appearing to the Ren'Py Store
renpy.store.__dict__.setdefault('Appearing', Appearing)

# Add Appearing to screen language
renpy.sl2.sldisplayables.DisplayableParser("appearing", Appearing, "default", 0)
# Register all valid parameters
renpy.sl2.sldisplayables.Positional("child")
for keyword in [ 'opaque_distance', 'transparent_distance' ]:
    renpy.sl2.sldisplayables.Keyword(keyword)

renpy.sl2.sldisplayables.add(renpy.sl2.slproperties.position_properties)

# Add as valid child for all containers
for i in renpy.sl2.slparser.childbearing_statements:
    i.add(renpy.sl2.slparser.all_statements[-1])
# Add as valid child for screens
renpy.sl2.slparser.screen_parser.add(renpy.sl2.slparser.all_statements[-1])

renpy.sl2.slparser.parser = None
