from parsimonious.grammar import Grammar

grammar = Grammar("""
   entry = street_number space street_name comma space city comma space zip_code comma space state comma space country_name
   street_number = number
   street_name = text
   city = text
   zip_code = number
   state = text
   country_name = text
   comma = ","
   space = " "
   number = ~"[0-9]*"i
   text = ~"[a-z]*"i
"""
                  )

parse_tree = grammar.parse("3945 Jackson, Memphis, 38019, TN, USA")
print(parse_tree)