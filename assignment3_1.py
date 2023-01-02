from parsimonious.grammar import Grammar

grammar = Grammar("""
   entry = (first_name space middle_name space last_name) / (first_name space last_name)
   
   first_name = text
   middle_name = text
   last_name = text
   space = " "
   text = ~"[a-z]*"i
"""
)

parse_tree = grammar.parse("Fatih Sen")
print(parse_tree)
