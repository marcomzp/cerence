#!/usr/bin/env python3

from symbol import Symbol

class Rule:

    def __init__(self, lhs, rhs):
        if (not lhs.isNonterminal()):
            raise RuntimeError("The left-hand side of a context-free rule must be a nonterminal, but " + lhs.__str__() + " is not")
        if not len(rhs) > 0:
            raise RuntimeError("The right-hand side of a context-free rule must be a non-empty list of Symbol objects")
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        rhsStrings = [str(rhs) for rhs in self.rhs]
        return str(self.lhs) + " → " + " ".join(rhsStrings)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return str(self) == str(other)
        else:
            return NotImplemented

    def __hash__(self):
        return hash(str(self))

    def __bool__(self):
        if len(self.rhs)==1 and self.rhs[0].isEpsilon():
            return False
        else:
            return True

    def __len__(self):
        if self:
            return len(self.rhs)
        else:
            return 0

    @staticmethod
    def readLine(line):
    
        parts = line.split()
        lhs = Symbol(parts[0])
    
        if len(parts) > 1:
            rhs = [Symbol(rhsString) for rhsString in parts[1:]]
            return Rule(lhs, rhs)

        else:
            rhs = [Symbol(None)]
            return Rule(lhs, rhs)

