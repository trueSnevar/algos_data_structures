# -*- coding: utf-8 -*-

def gen_parenthesis(n: int, prefix: str, opened: int, close: int):
    """ Given n pairs of parentheses, 
    write a function to generate all combinations 
    of well-formed parentheses.
    
    Example input: 2
    Output: (())
            ()()
            
    """

    if opened == close == n:
        print(prefix)
    if opened < n:
        gen_parenthesis(n, prefix + '(', opened+1, close)
    
    if close < opened:
        gen_parenthesis(n, prefix + ')', opened, close+1)

if __name__ == "__main__":
    n = int(input())
    gen_parenthesis(n, "", 0, 0)