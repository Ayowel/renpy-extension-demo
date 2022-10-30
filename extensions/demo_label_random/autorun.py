# This is based on the documentation example available at
# https://www.renpy.org/doc/html/cds.html
from demo_label_random import lint_random, next_random, parse_random
import renpy

# Add custom label to Ren'Py
renpy.statements.register(
    name="random",
    block=True,
    parse=parse_random,
    next=next_random,
    lint=lint_random,
)
