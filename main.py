"""
    Extend the buildParseTree function to handle mathematical expressions
    that do not have spaces between every character.
"""
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


def buildParseTree(fpexp):
    fplist = []
    num = ''

    for ch in fpexp:
        if ch not in ['(', '+', '-', '*', '/', ')']:
            if num == '':
                num = ch
            else:
                num = num + ch
        else:
            if num != '':
                fplist.append(num)
            fplist.append(ch)
            num = ''

    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        else:
            raise ValueError
    return eTree


pt = buildParseTree("((10+5)*3)")
pt.postorder()
