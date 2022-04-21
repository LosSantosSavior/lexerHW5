#COMP340
#Nicholas Russell

import lexer

srcCode = "((12+3*5)+5/4)"
tokSeq = lexer.tokenize(srcCode)

for eachTok in tokSeq:
    print(eachTok.type, eachTok.value)

