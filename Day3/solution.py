import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Serialized representation {value: '<>', left: {...}, right: {...}}
def serialize(node):
    return json.JSONEncoder()\
        .encode(return_repr(node))

def return_repr(node):
    if not node:
        return None

    repr = {
        'value': node.val,
        'left': return_repr(node.left),
        'right': return_repr(node.right)
    }
    return repr

def deserialize_object(obj):
    if not obj:
        return None

    return Node(obj['value'], deserialize_object(obj['left']), deserialize_object(obj['right']))

def deserialize(string):
    repr_object = json.JSONDecoder().decode(string)
    return deserialize_object(repr_object)

def test_solution():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
