from dragonfly.actions.action_text import Text
from dragonfly.grammar.rule_mapping import MappingRule

__author__ = 'parkerh'


class PutStringCommandsRule(MappingRule):
    mapping = {
        "put e-mail": Text("petkoxray@gmail.com"),
        "put first": Text("Petko"),
        "put last": Text("Kostadinov"),
        "put [whole] name": Text("Petko Kostadinov"),
        "put address": Text("Vasil Chekalarov 8"),
        "put city": Text("Plovdiv"),
        #"put state": Text("CA"),
        #"put zip": Text("94901"),
        #"put phone": Text("415 297 6170"),
        #"put Google phone": Text("415 548 1460"),
        #"put user": Text("haughki"),
        # "put Dragon info": Text("NatLink 4.1mike\nDNS 13\nPython 2.7\nWindows 7"),
        }
