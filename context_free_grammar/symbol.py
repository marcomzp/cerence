#!/usr/bin/env python3

class Symbol:

    def __init__(self, value):
        if value is None:
            self.value = None
        else:
            self.value = str(value)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.value)
    
    def __str__(self):
        if self:
            return self.value
        else:
            return "ε"

    def __bool__(self):
        if (self.value==None):
            return False
        else:
            return True        

    def __len__(self):
        if self:
            return len(str(self))
        else:
            return 0

    def isEpsilon(self):
        return not bool(self)

    def isNonterminal(self):
        if self:
            if self.value[0].isupper():
                return True
            else:
                return False
        else:
            return False

    def isTerminal(self):
        if self:
            return not self.isNonterminal()
        else:
            return False


if __name__ == "__main__":

    x = Symbol(None)
    y = Symbol("NP")

    if x:
        print("Our symbol is not epsilon")
    else:
        print("Our symbol is epsilon")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    print(x is y)
    print(x == y)
    print(len(symbols))
