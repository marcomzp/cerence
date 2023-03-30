#!/usr/bin/env python3

import sys
#import intertools 

def PowerSet(seq):
	result = [[]]
	for rule in seq:
		result.extend([x + [rule] for x in result])
	return result[1:]


class Symbol:

	symbols = {}

	def __init__(self, value):
		self.value = value

	def __str__(self):
		if (self.isEpsilon()):
			return "ε"
		else:
			return self.value.__str__()

	@staticmethod
	def get(key):
		if key in Symbol.symbols:
			return Symbol.symbols[key]
		else:
			value = Symbol(key)
			Symbol.symbols[key] = value
			return value

	def isEpsilon(self):
		if (self.value==None):
			return True
		else:
			return False

	def isNonterminal(self):
		if self.isEpsilon():
			return False
		else:
			if self.value[0].isupper():
				return True
			else:
				return False

	def isTerminal(self):
		if self.isEpsilon():
			return False
		else:
			return not self.isNonterminal()


class Rule:

	def __init__(self, lhs, rhs):
		if (not lhs.isNonterminal()):
			raise RuntimeError("The left-hand side of a context-free rule must be a nonterminal, but " + lhs.__str__() + " is not")
		self.lhs = lhs
		self.rhs = rhs

	def __str__(self):
		rhsStrings = [rhs.__str__() for rhs in self.rhs]
		return self.lhs.__str__() + " → " + " ".join(rhsStrings)

	@staticmethod
	def readLine(line):
	
		parts = line.split()
		lhs = Symbol.get(parts[0])
	
		if len(parts) > 1:
			rhs = [Symbol.get(rhsString) for rhsString in parts[1:]]
			return Rule(lhs, rhs)

		else:
			rhs = [Symbol.get(None)]
			return Rule(lhs, rhs)


class Grammar:

	def __init__(self, rules):
		self.rules = rules

	@staticmethod
	def readLines(file):

		rules = []
		for line in file:
			rule = Rule.readLine(line)
			rules.append(rule)
		return Grammar(rules)


	def findInitiallyNullableSymbols(self):
		result = set()
		for rule in self.rules:
			if len(rule.rhs) == 1 and rule.rhs[0].isEpsilon():
				result.add(rule.lhs)
		return result
			 

	def findMoreNullableSymbols(self, nullableSymbols):
		result = set()
		for rule in self.rules:
			are_all_symbols_null = True 
			for symbol in rule.rhs:
				if symbol not in nullableSymbols:
					are_all_symbols_null = False
			if are_all_symbols_null == True and rule.lhs not in nullableSymbols:   
				result.add(rule.lhs)
		return result 
		
		"""Given a set of nullable symbols, returns a new set of nullable symbols.
		   The returned set will consist of symbols that appear on the left-hand side of rules.
		   in which all symbols on the right-hand side are in the initial set of nullable symbols"""
	   

	def findNullableSymbols(self):
		InitiallyNullableSymbols = self.findInitiallyNullableSymbols()
		MoreNullableSymbols = self.findMoreNullableSymbols(InitiallyNullableSymbols)
		NullableSymbols = MoreNullableSymbols|InitiallyNullableSymbols
		NullableSymbols2 = self.findMoreNullableSymbols(NullableSymbols)
		while len(NullableSymbols2) != 0:
			NullableSymbols = NullableSymbols|NullableSymbols2 
			NullableSymbols2 = self.findMoreNullableSymbols(NullableSymbols)
		return NullableSymbols
		
		 
		
		"""Returns all nullable symbols in this grammar"""
	  
	  
		# Step 1: findInitiallyNullableSymbols

		# Step 2: use the results from step 1 to call findMoreNullableSymbols

		# Step 3: add the newly nullable symbols to the set of nullable symbols

		# Step 4: use the results from step 3 to call findMoreNullableSymbols

		# ... repeat steps 3 and 4 until the results of step 4 is the empty set

		# Return the set of nullable symbols
		pass

	def removeEpsilons(self):
		NullableSymbols = self.findNullableSymbols()
		NoEpsilonRules = set()
		

		for rule in self.rules:
			notnullable = []
			for symbol in rule.rhs:
				if  (symbol not in NullableSymbols) and (not symbol.isEpsilon()):
					#print(symbol)
					notnullable.append(symbol)
			#print(notnullable)
			if len(notnullable) == len(rule.rhs):
				#print(rule)
				NoEpsilonRules.add(rule)
			else:
				powerset = PowerSet(rule.rhs)
				for symbols in powerset:
					newRule = Rule(rule.lhs, symbols)
					#print(newRule)
					notnullable2 = []
					for symbol2 in newRule.rhs: 
						if (symbol2 not in NullableSymbols) and (not symbol2.isEpsilon()):
							#print(symbol2)
							notnullable2.append(symbol2)
					#notnullable2 = [symbol not in NullableSymbols for symbol in newRule.rhs]
					if len(notnullable2) == len(newRule.rhs):
						NoEpsilonRules.add(newRule)

		"""Returns an equivalent grammar that contains no epsilons"""  
		return Grammar(NoEpsilonRules)

	def removeUnaryRules(self): #eliminate variable productions
		"""Returns an equivalent grammar 
		that contains no unary-branching rules in which the right-hand side is a non-terminal"""
		NullableSymbols = self.findNullableSymbols()
		notUnaryRule = set()

		for rule in self.rules:
			powerset = PowerSet(rule.rhs)
			for symbols in powerset:
				newRule = Rule(rule.lhs, symbols)
				print(newRule, newRule.rhs[0])
				if (len(newRule.rhs) >= 2) or (newRule.rhs[0].isTerminal()):
					print("this is new rule", newRule)
					notUnaryRule.add(newRule)

		return Grammar(notUnaryRule)


		
	def shortenLongRules(self):
		shortRule = set()
		for rule in self.rules:
			powerset = PowerSet(rule.rhs)
			for symbols in powerset:
				newRule = Rule(rule.lhs, symbols)
				if len(newRule.rhs) <= 2:
					shortRule.add(newRule)

		return Grammar(shortRule)

		"""Returns an equivalent grammar in which the right-hand side of every rule contains no more than two symbols"""
		
		
	def makeTerminalsUnary(self):
		print("this is makeTerminalsUnary")
		counter = 0
		replacementLabel = "X"
		terminalUnary = set()
		for rule in self.rules:
			terminalSymbols = [(symbol, rule.rhs.index(symbol)) for symbol in rule.rhs if symbol.isTerminal()]
			#print(terminalSymbols)
			if len(terminalSymbols) >= 1 and len(rule.rhs) >= 2:
				for pair in terminalSymbols:
					counter = counter + 1
					currentString = replacementLabel + str(counter)
					newSymbol = Symbol.get(currentString)
					newRule = Rule(newSymbol, [pair[0]])
					terminalUnary.add(newRule)
					rule.rhs[pair[1]] = newSymbol
				terminalUnary.add(rule)	

		return Grammar(terminalUnary)


		#for rule in self.rules:
			#if rule.rhs


		

		#if we have any rule where there is a terminal on the right hand side, I would introduce
		#new rules with dummy non-terminals (T)
		#S --> A b C d (the lower case are terminals) 
		# S --> A T1 C T2
		# T1 -> b
		# T2 -> d
		#write unitests to test these things. 

		##Returns an equivalent grammar 
		##where every terminal is found only as the right-hand side of a unary-branching rule
		
	   



if __name__ == "__main__":

	if len(sys.argv) < 2:

		print("Please provide a file as argument")


	else:

		fileName = sys.argv[1]

		with open(fileName) as file:

			grammar = Grammar.readLines(file)
			grammar2 = grammar.removeEpsilons()
			grammar3 = grammar.removeUnaryRules()
			grammar4 = grammar.shortenLongRules()
			print("before grammar5")
			grammar5= grammar.makeTerminalsUnary()
			#grammar3 = grammar.removeUnaryRules()
			#nullableSymbols = grammar.findNullableSymbols()
			print("This is the grammar without epsilons")
			for rule in grammar2.rules:
				print(rule)
			print("This is the Unary grammar")
			for rule in grammar3.rules:
				print(rule)
			print("This is the short grammar")
			for rule in grammar4.rules:
				print(rule)
			print("This is grammar5")
			for rule in grammar5.rules:
				print(rule)









		