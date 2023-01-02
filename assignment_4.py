from parsimonious.grammar import Grammar

grammar = Grammar("""
   sentence = pronoun space verb space adj space noun  space conj space pronoun space verb space pronoun
  
   space = " "
   pronoun = ~"[a-z]*"i
   verb = ~"[a-z]*"i
   adj = ~"[a-z]*"i
   noun = ~"[a-z]*"i
   conj = ~"[a-z]*"i
   pronoun = ~"[a-z]*"i
   verb = ~"[a-z]*"i
   pronoun = ~"[a-z]*"i
"""
)

parse_tree = grammar.parse("She likes big snakes but I hate them")
print(parse_tree)