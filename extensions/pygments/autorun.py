import pygments
from pygments.formatter import Formatter
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Token, Whitespace
from pygments.util import get_choice_opt
import renpy

# Map token types to a tuple of color values for light and dark
# backgrounds.
# This was only checked on a dark background
COLORS = {
    Token:              ('', ''),

    Whitespace:         ('#808080', '#778899'),
    Comment:            ('#007000', '#007000'),
    Comment.Preproc:    ('#007000', '#007000'),
    Keyword:            ('#800080', '#800080'),
    Keyword.Type:       ('#0000ff', '#0000ff'),
    Operator.Word:      ('#1E90FF', '#1E90FF'),
    Name.Builtin:       ('#00FFFF', '#E0FFFF'),
    Name.Function:      ('#008000', '#90EE90'),
    Name.Namespace:     ('#00FFFF', '#00FFFF'),
    Name.Class:         ('_#008000_', '#90EE90'),
    Name.Exception:     ('#00FFFF', '#E0FFFF'),
    Name.Decorator:     ('#778899', '#808080'),
    Name.Variable:      ('#ff0000', '#FFB6C1'),
    Name.Constant:      ('#ff0000', '#FFB6C1'),
    Name.Attribute:     ('#00FFFF', '#E0FFFF'),
    Name.Tag:           ('#ADD8E6', '#ADD8E6'),
    String:             ('#D48440', '#D48440'),
    Number:             ('#008000', '#008000'),

    Generic.Deleted:    ('#FFB6C1', '#FFB6C1'),
    Generic.Inserted:   ('#008000', '#90EE90'),
    Generic.Heading:    ('**', '**'),
    Generic.Subheading: ('*#FF00FF*', '*#F08080*'),
    Generic.Error:      ('#FFB6C1', '#FFB6C1'),

    Error:              ('_#FFB6C1_', '_#FFB6C1_'),
}

# Add text tags to format it for Ren'Py
def colorformat(color, text):
    if len(color) < 1:
        return text
    add = ''
    sub = ''
    if '_' in color:
        add += '{i}'
        sub = '{/i}' + sub
        color = color.strip('_')
    if '*' in color:
        add += '{b}'
        sub = '{/b}' + sub
        color = color.strip('*')
    if len(color) > 0:
        add += '{color=%s}' % color
        sub = '{/color}' + sub
    return add + text + sub

# Formatter used to generate strings usable in Ren'Py's text Displayables
class RenPyFormatter(Formatter):
    name = 'RenPy'
    aliases = ['rpy', 'RPY', 'Renpy']
    filenames = []

    def __init__(self, **options):
        super(RenPyFormatter, self).__init__(**options)
        self.darkbg = get_choice_opt(options, 'bg',
                                     ['light', 'dark'], 'light') == 'dark'
        self.colorscheme = options.get('colorscheme', None) or COLORS
        self.linenos = options.get('linenos', False)
        self._lineno = 0
        self.linecount_size = options.get('linecount_size', 3)

    def _write_lineno(self, outfile):
        if self.linenos:
            self._lineno += 1
            outfile.write(("{color=#888}%0" + str(self.linecount_size) + "d:{/color} ") % self._lineno)

    def format_unencoded(self, tokensource, outfile):
        self._write_lineno(outfile)

        for ttype, value in tokensource:
            value = value.replace('{', '{{')
            color = self.colorscheme.get(ttype)
            while color is None:
                ttype = ttype[:-1]
                color = self.colorscheme.get(ttype)
            if color:
                color = color[self.darkbg]
                spl = value.split('\n')
                for line in spl[:-1]:
                    if line:
                        outfile.write(colorformat(color, line))
                    outfile.write('\n')
                    self._write_lineno(outfile)
                if spl[-1]:
                    outfile.write(colorformat(color, spl[-1]))
            else:
                outfile.write(value)

# Make the formatter available natively in Ren'Py
renpy.store.__dict__.setdefault('RenPyFormatter', RenPyFormatter)
