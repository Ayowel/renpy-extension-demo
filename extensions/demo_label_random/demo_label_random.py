import random
import renpy

def parse_random(lexer):
    subblock_lexer = lexer.subblock_lexer()
    choices = []

    while subblock_lexer.advance():
        with subblock_lexer.catch_error():
            statement = subblock_lexer.renpy_statement()
            choices.append(statement)

    return choices

def next_random(choices):
    return random.choice(choices)

def lint_random(parsed_object):
    for i in parsed_object:
        renpy.text.extras.check_text_tags(i)
