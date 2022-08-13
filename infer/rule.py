from unicodedata import name

class Rule:
    def __init__(self, name, value=0.0, parent=None, children=[]):
        self.name = name
        self.value = value
        self.parent = parent
        self.children = children

    def propagate(self):
        pass

            
def propagateAll(topRule):
    children = topRule.children
    out = 1.0
    if len(children):
        for child in children:
            out *= propagateAll(child)
    else:
        out = topRule.value
    topRule.value = out
    return out 

  
def parseRulesFromJson():
    pass

if __name__=="__main__":
    rule1 = Rule("rule1", 2)
    rule2 = Rule("rule2", 3)
    rule3 = Rule("rule3", 4, children=[rule1, rule2])
    propagateAll(rule3)
    print(rule3.value)