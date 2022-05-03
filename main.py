#COMP340
#Nicholas Russell

import lexer
import parserr

srcCode = "1 * (2 + 5)"
tokSeq = lexer.tokenize(srcCode)
rootNode = parserr.parse(tokSeq)
parserr.printTree(rootNode)
print()