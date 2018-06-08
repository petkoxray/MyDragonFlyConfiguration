from dragonfly import (BringApp, StartApp, Key, Function, Grammar, Playback, Mouse, Choice,
                       Dictation, MappingRule, Text, Integer, CompoundRule, AppContext)
import logging
import logging.handlers

import dragonfly.log as log
from pywinauto.application import Application
from pywinauto import findwindows
log.setup_log()


def NavigationFunction():
    app = Application(backend='win32')
    # app.connect(path= r"C:\Program Files (x86)\Microsoft VS Code Insiders\Code - Insiders.exe")
    # app.connect(path= r"C:\Program Files (x86)\Microsoft VS Code\Code.exe")
    app.connect(path=r"c:\Windows\Explorer.exe")
#    print findwindows.find_elements()
    # app.top_window().menu_select("Help->About")
    # print app.windows()

    app.CabinetWClass.SysTreeView321.click()
    app.CabinetWClass.SysTreeView321.TypeKeys(" ")


def FilePaneFunction():
    app = Application(backend='win32')
    # app.connect(path= r"C:\Program Files (x86)\Microsoft VS Code Insiders\Code - Insiders.exe")
    # app.connect(path= r"C:\Program Files (x86)\Microsoft VS Code\Code.exe")
    app.connect(path=r"c:\Windows\Explorer.exe")
#    print findwindows.find_elements()
    # app.top_window().menu_select("Help->About")
    # print app.windows()

    app.CabinetWClass.DirectUIHWND3.TypeKeys(" ")
    app.CabinetWClass.DirectUIHWND3.click()


class MainRule(MappingRule):
    mapping = {
        # "Skype Mary":                  StartApp(r"c:\program files (x86)\Skype\phone\Skype", r"/callto:mtsangarakis"),
        # "connect house":               BringApp(r"c:\program files\realvnc\vnc5\vncviewer5", r"192.168.1.132"),
        # "file pane":                   Key("c-p"),
        # "inspect element":             Key("shift:down") + Mouse("right:1") + Key("shift:up"),
#        "menu about":                   Function(menuFunction),
        "test search":                   Text("{w}editorr"),
        "duplicates search":                   Text("{d}"),

        "click help":                  Key("cs-u"),
        "show Explorer":               Key("cs-e"),
        "show files":                  Key("cas-e"),
        "show editors":                Key("c-k/60,e"),
        "show Extensions":             Key("cs-x"),
        "show git":                    Key("cs-g"),
        "show debugger":               Key("cs-d"),
        "show output":                 Key("cs-u"),
        "show problems":               Key("cs-m"),
        "show debug output":           Key("cs-y"),

        "show terminal":               Key("cas-backtick"),
        "toggle terminal":             Key("c-backtick"),
        "new terminal":                Key("cs-backtick"),
        "kill terminal":               Key("cas-quote"),
        "clear terminal":              Key("c-k"),
        "toggle sidebar":              Key("c-b"),
        "expand view [<ln>]":          Key("ca-b:%(ln)d"),
        "contract view [<ln>]":        Key("ca-e:%(ln)d"),
        "toggle panel":                Key("c-j"),
        "show key bindings":           Key("c-k/20,c-s"),
        "toggle developer":            Key("c-f1"),

        
        # File and Folder operations
        "open folder":                 Key("c-k,c-o"),
        "open recent":                 Key("c-r,r"),

        # "follow <ln>":                 Text("%(ln)d\r"),
        # "<password> secret":            Text("%(password)s\r"),
        #"special mode":                Function(my_function),                            '''
        "pop up":                      Key("s-f10"),
        "drop down":                      Key("a-down"),
        "save as":                     Key("cs-s"),

        # Navigation Commands

        "scroll up [<ln>]":              Key("c-up:%(ln)d"),
        "scroll down [<ln>]":            Key("c-down:%(ln)d"),


        "add line comment":              Key("c-k,c-c"),
        "toggle comment":              Key("c-slash"),
        "toggle block comment":              Key("as-a"),

        "show clipboard":              Key("ca-v"),
        "cycle clipboard":              Key("cs-v"),

        "find":                        Key("c-f"),
        "replace symbol":              Key("f2"),
        "insert snippet":              Key("c-k/50,c-q"),


        "fold all":                    Key("c-k/50,c-0"),
        "fold one":                    Key("c-k/50,c-1"),
        "fold two":                    Key("c-k/50,c-2"),
        "fold here":                    Key("cs-lbracket"),
        "unfold here":                    Key("cs-rbracket"),
        "unfold all":                  Key("c-k/50") + Key("c-j"),

        "toggle bookmark":             Key("ca-k"),
        "next bookmark":               Key("ca-l"),
        "previous bookmark":           Key("cas-q"),
        "list bookmarks":               Key("cas-l"),

        "next change":               Key("cas-n"),

        # GIT Commands
        "merge current":                 Key("c-r/50,c"),
        "merge incoming":                Key("c-r/50,i"),
        "merge both":                    Key("c-r/50,b"),
        # FTP-sync extension commands
        "sync current file":        Key("c-k/50,ca-s"),
        # git commands
        "github URL":               Text("https://github.com/cleidigh/"),

        # Debugging commands
        "Debug run":                 Key("f5"),
        "Debug stop":                Key("s-f5"),
        "toggle breakpoint":         Key("f9"),
        "step over":                 Key("f10"),
        "step into":                 Key("f11"),
        "Debug start":               Key("ca-slash/60") + Text("Launch V") + Key("enter/50"),
        "Attach start":               Key("ca-slash/60") + Text("Attach to V") + Key("enter/50"),
        # "Attach start":               Key("f1/60") + Text("debug sel")  + Key("enter/50")+ Key("A/50,t,enter"),

        "Run OSS":                    Key("c-r,o"),
        "Test Messages":                    Key("c-r,t"),
        "Test two Messages":                    Key("c-r,u"),
        "Focus Messages":                    Key("c-r,f"),
        "Click terminal link":        Key("alt:down")+Mouse("left:1")+Key("alt:up"),
        "Click terminal link Control":        Key("control:down")+Mouse("left:1")+Key("control:up"),
        "Click mac terminal link":        Key("win:down")+Mouse("left:1/30")+Key("win:up"),
        # runner extension commands

        "run commands":               Key("cas-c"),

        # typegrandma
        "triple equals":              Text(" === "),

        "color theme":               Key("c-k/20,c-t"),

        "color white":               Text("#ffffff"),
        "color black":               Text("#000000"),
        "color blue":               Text("#000080"),
        "color green":               Text("#008000"),
        "color red":               Text("#800000"),
        "color yellow":               Text("#909800"),
        "color Brown":               Text("#503020"),
        "console output":               Text("console.debug('');"),
        "console log":               Text("console.log('');"),
        "terminal test one":        Key('cs-backtick,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6:10'),
        "terminal test two":        Key('cs-backtick,1,2,3,4,5,6:10,enter,d,i,r,enter,1:30,X,enter,1:40/10,X'),
        "terminal test three":        Key('cs-backtick/100,a'),

    }

    extras = [Integer("ln", min=1, max=500),
              Dictation("text"),
              Choice("password", {"admin": "kounavoi", "mac": "skatulaki"})]

    defaults = {"ln": 1,
                "text": "",
                }

#    def _process_begin(node):
#        print "utterance"
#        print node

context = AppContext(executable="code")
grammar = Grammar("vs_code_general", context=context)
grammar = Grammar('sample')
grammar.add_rule(MainRule())
grammar.load()

#print("loaded dfnl1 1")

# Unload function which will be called by natlink at unload time.


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None