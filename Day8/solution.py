import copy
class Tree():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.isunival = None
        self.left = left
        self.right = right


def isUnival(tree):
    '''
    We use memoization to solve our problem. The status about the unival is stored with each node
    :param tree:
    :return:
    '''
    if tree.isunival is not None:
        return tree.isunival
    boolUnival = True
    if tree.left and tree.left.value != tree.value:
        tree.isunival = False
        return False
    if tree.right and tree.right.value != tree.value:
        tree.isunival = False
        return False

    leftunival = True
    rightunival = True
    if tree.left:
        leftunival = leftunival and isUnival(tree.left)
    if tree.right:
        rightunival = rightunival and isUnival(tree.right)

    return leftunival and rightunival


def getNumUnivalSubtrees(tree):
    num_unival = 0
    if not tree:
        return 0
    if isUnival(tree):
        num_unival+=1
    num_unival += getNumUnivalSubtrees(tree.left) + getNumUnivalSubtrees(tree.right)
    return num_unival


def test_solution():
    # Construct tree
    tree = Tree(
        0, left=Tree(1), right=Tree(0,
                    left=Tree(1, left=Tree(1), right=Tree(1)), right=Tree(0)))

    assert getNumUnivalSubtrees(tree) == 5
