from collections import deque


PARENS = ("(", ")")
BRACKETS = ("[", "]")
CHARS = ("", ";", " ", "\\", "\t")
EMPTY, SEMICOLON, SPACE, SLASH, TAB = CHARS
VALIDATION = {
    "tree": "tree missing",
    "node": "tree with no nodes",
    "delimiter": "properties without delimiter",
    "uppercase": "property must be in uppercase",
}


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or deque()

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    """parse an SGF string and return a tree structure of properties."""

    _validate_is_tree_with_node(input_string)

    stack = list(input_string)
    tree = SgfTree()
    prop = {}
    value = deque()
    is_value = False
    

    while stack:
        current = stack.pop()
        _validate_delimiters(value, is_value, current)

        if current in PARENS:
            continue
        elif current == SEMICOLON:
            _add_node(tree, prop)
        elif is_value and current != BRACKETS[0]:
            current = _replace_slashes_and_tabs(current)
            if current:
                _add_current_to_value(stack, value, current)
        elif current in BRACKETS:
            is_value = not is_value
        else:
            _validate_property_is_uppercase(current)
            _add_property(prop, value, current)

    return tree


def _add_node(tree, prop):
    if not tree.properties:
        tree.properties = prop.copy()
    else:
        tree.children.appendleft(SgfTree(tree.properties))
        tree.properties = prop.copy()
    
    prop.clear()


def _replace_slashes_and_tabs(current):
    if current == SLASH:
        current = EMPTY
    elif current == TAB:
        current = SPACE

    return current


def _add_current_to_value(stack, value, current):
    if stack and stack[-1] != BRACKETS[0] and value:
        value[0] = current + value[0]
    else:
        value.appendleft(current)


def _add_property(prop, value, current):
    prop[current] = list(value)
    value.clear()


def _validate_is_tree_with_node(input_string):
    if input_string in CHARS[:2]:
        raise ValueError(VALIDATION["tree"])

    elif input_string == "".join(PARENS):
        raise ValueError(VALIDATION["node"])


def _validate_delimiters(value, is_value, current):
    if not value and not is_value and current.isalpha():
        raise ValueError(VALIDATION["delimiter"])


def _validate_property_is_uppercase(current):
    if not current.isupper():
        raise ValueError(VALIDATION["uppercase"])
