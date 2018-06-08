"""A command module for Dragonfly, for controlling IntelliJ IDEA-based IDEs.

taken from nirvdrum"s module at:
https://github.com/dictation-toolbox/dragonfly-scripts/blob/master/_app_intellij.py
-----------------------------------------------------------------------------
Licensed under the LGPL3.

"""
from dragonfly import Function
from dragonfly import Grammar, MappingRule, Dictation, Integer, Key, Text, IntegerRef, AppContext
from supporting import utils

def getFile(text=None):
    open_get_file_dialog = Key("cas-n")
    if text:
        open_get_file_dialog.execute()
        file_name = str(text).lower()
        Text(file_name).execute()
    else:
        open_get_file_dialog.execute()

def printNumber(w, x=None, y=None, z=None):
    number = utils.buildNumber(w, x, y, z)
    Text(number).execute()

class CommandRule(MappingRule):
    mapping = {
		#Terminal
        "toggle terminal":             Key("c-backtick"),
        "clear terminal":              Key("c-k"),
		
		#Navigation
		"toggle sidebar":              Key("c-b"),
		"toggle panel":                Key("c-j"),
		"find":                        Key("c-f"),

		
		#App
		"open file": Key("c-p"),
		"run app": Key("ca-n"),
		"format document": Key("ca-l"),
		
        # Debugging commands
        "Debug run":                 Key("f5"),
        "Debug stop":                Key("s-f5"),
        "toggle breakpoint":         Key("f9"),
        "step over":                 Key("f10"),
        "step into":                 Key("f11"),
        "Debug start":               Key("ca-slash/60") + Text("Launch V") + Key("enter/50")
        #"Attach start":               Key("ca-slash/60") + Text("Attach to V") + Key("enter/50")
        # Custom key mappings.
        # "(run SSH session|run SSH console|run remote terminal|run remote console)": Key("a-f11/25, enter"),
    }
    extras = [
        Integer("t", 1, 50),
        Dictation("text"),
        IntegerRef("n", 1, 50000),
        Integer("w", 0, 10),
        Integer("x", 0, 10),
        Integer("y", 0, 10),
        Integer("z", 0, 10),
    ]
    defaults = {
        "t": 1,
    }


context = AppContext(executable="code")
idea_grammar = Grammar("code", context=context)
idea_grammar.add_rule(CommandRule())
idea_grammar.load()

def unload():
    global idea_grammar
    idea_grammar = utils.unloadHelper(idea_grammar,__name__)