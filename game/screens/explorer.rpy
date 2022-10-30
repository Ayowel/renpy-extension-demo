init python:
    import math
    import pygments
    import zipfile
    from pygments.lexers import PythonLexer

default extensions_list = ['demo_warper', 'demo_label_random', 'demo_appearing', 'pygments']
default overview_mode = False
default current_extension = None

init python:
    def init_extension(extension_name):
        archive_files = []
        if renpy.loadable("{}.rpe".format(current_extension)):
            with renpy.open_file("{}.rpe".format(current_extension), False) as f:
                with zipfile.ZipFile(f, 'r') as z:
                    archive_files = z.namelist()
        renpy.run([
            SetScreenVariable('archive_files', archive_files),
            SetScreenVariable('current_file', None),
            SetScreenVariable('current_file_content', None),
            ])

    def inject_file(path, content):
        if path.endswith('.py') or path.endswith('.rpy'):

            content = pygments.highlight(content, PythonLexer(), RenPyFormatter(linecount_size = len(str(content.count("\n")+1)), linenos = True))
        renpy.run([
            SetScreenVariable('current_file', path),
            SetScreenVariable('current_file_content', content),
        ])

    def load_file(path):
        if renpy.loadable(path):
            with renpy.open_file(path) as f:
                content = f.read().decode('utf-8')
            inject_file(path, content)

    def load_extension_file(extpath, path):
        if renpy.loadable(extpath):
            with renpy.open_file(extpath) as zf:
                with zipfile.ZipFile(zf, 'r') as z:
                    if path in z.namelist():
                        content = z.read(path).decode('utf-8')
                    inject_file("{}/{}".format(extpath, path), content)

screen file_explorer():
    default last_current_extension = None
    default current_file = ''
    default current_file_content = ''
    default archive_files = []
    python:
        if last_current_extension != current_extension:
            last_current_extension = current_extension
            init_extension(current_extension)
    vbox:
        if overview_mode:
            viewport:
                ysize 90
                draggable True
                scrollbars 'horizontal'
                hbox:
                    spacing 30
                    textbutton '{b}{size=+10}< Back{/size}{/b}':
                        action [SetVariable('current_extension', None), Return()]
                    for e in extensions_list:
                        textbutton e:
                            action SetVariable('current_extension', e)
                            yalign 0.5

        if current_extension is not None:
            hbox:
                if not overview_mode:
                    ysize 800
                else:
                    ysize 990
                vbox:
                    xsize config.screen_width - 600
                    if current_file_content:
                        text "{size=+10}%s{/size}" % (" > ".join(current_file.split("/"))):
                            substitute False
                            xoffset 30
                        viewport:
                            scrollbars 'both'
                            draggable True
                            text "[current_file_content]"
                viewport:
                    xsize 600
                    scrollbars 'vertical'
                    draggable True
                    vbox:
                        xsize 580
                        if renpy.loadable("examples/{}.rpy".format(current_extension)):
                            textbutton "examples/{}.rpy".format(current_extension):
                                action Function(load_file, "examples/{}.rpy".format(current_extension))
                        textbutton "Extension content:"
                        for f in archive_files:
                            textbutton f:
                                xoffset 40
                                action Function(load_extension_file, "{}.rpe".format(current_extension), f)
