# The following "Appearing" class is part of the official Ren'Py documentation
# and is under MIT License
import math
import renpy

class Appearing(renpy.display.core.Displayable):
    # Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    # The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    def __init__(self, child, opaque_distance, transparent_distance, **kwargs):

        # Pass additional properties on to the renpy.Displayable
        # constructor.
        super(Appearing, self).__init__(**kwargs)

        # The child.
        self.child = renpy.easy.displayable(child)

        # The distance at which the child will become fully opaque, and
        # where it will become fully transparent. The former must be less
        # than the latter.
        self.opaque_distance = opaque_distance
        self.transparent_distance = transparent_distance

        # The alpha channel of the child.
        self.alpha = 0.0

        # The width and height of us, and our child.
        self.width = 0
        self.height = 0

    def render(self, width, height, st, at):

        # Create a transform, that can adjust the alpha channel of the
        # child.
        t = renpy.display.transform.Transform(child=self.child, alpha=self.alpha)

        # Create a render from the child.
        child_render = renpy.display.render.render(t, width, height, st, at)

        # Get the size of the child.
        self.width, self.height = child_render.get_size()

        # Create the render we will return.
        render = renpy.display.render.Render(self.width, self.height)

        # Blit (draw) the child's render to our render.
        render.blit(child_render, (0, 0))

        # Return the render.
        return render

    def event(self, ev, x, y, st):

        # Compute the distance between the center of this displayable and
        # the mouse pointer. The mouse pointer is supplied in x and y,
        # relative to the upper-left corner of the displayable.
        distance = math.hypot(x - (self.width / 2), y - (self.height / 2))

        # Base on the distance, figure out an alpha.
        if distance <= self.opaque_distance:
            alpha = 1.0
        elif distance >= self.transparent_distance:
            alpha = 0.0
        else:
            alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

        # If the alpha has changed, trigger a redraw event.
        if alpha != self.alpha:
            self.alpha = alpha
            renpy.display.render.redraw(self, 0)

        # Pass the event to our child.
        return self.child.event(ev, x, y, st)

    def visit(self):
        return [ self.child ]
