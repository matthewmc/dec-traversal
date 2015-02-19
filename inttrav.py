from collections import deque
from random import choice

# Function that takes a custom class and seeks out attributes referencing
# objects of the same type.  
# Priority rules as follows:
# 1. Iterable attributes
# 3. Attributes

# To do:
# 2. Custom containers
# 3a. OrderedDict
# 4. Nested iterables()
def prioritize(obj):
    type_ = type(obj)
    attrs = obj.__dict__

    def get_items(attributes):
        results = [item for key, item in attributes.items() if type(item) == type_]
        if results != None:
            return results
        elif results == None:
            return []
    # Case 1
    res = []
    for key, item in attrs.items():
        if type(item) == list or type(item) == tuple:
            try:
                res.extend([x for x in item if type(x) == type_])
            except TypeError:
                pass
        elif type(item) == dict:
            res += get_items(item)    
        elif type(item) != int and type(item) != str and type(item) != bool:
            try:
                prioritize(item)
            except:
                pass
    if len(res) > 0:
        return res

    """
    # Case 2:
    for key, item in attrs.items():
        if True:
            try:
                res += prioritize(item)
            except:
                print('Encountered error recursing.')
    if len(res) > 0:
        return res
    """
    # Case 3 
    res = get_items(attrs)
    if len(res) > 0:
        return res

    # On failed search.
    else:
        return None

def bfs_path(Node, queue, visited):
    visited.add(Node)    
    try:
        # Add neighbor nodes only if not already visited or in queue.
        queue.extend([x for x in prioritize(Node) if x not in visited and x not in queue])
    except TypeError:
        pass


def dfs_path(Node, queue, visited):
    visited.add(Node)
    try:
        queue.extendleft([x for x in prioritize(Node) if x not in visited and x not in queue])
    except TypeError:
        pass
"""
To do: Random walks

def rand_walk(Node, queue, visited):
    try:
        queue.append(choice(prioritize(Node)))
    except TypeError:
        pass
"""

"""
To do: 
Refactor with another decorator to clean up the three 
decorators below.
"""

# Decorates given function which takes a generic node-style object
# and runs that function at each node on the path dictated by decorator.
# Expects a tuple returned at each node
# containing (bool that represents whether traversal should continue, 
#             optional result that will be appended and returned.)
def bfs(func):
    # Wrapper that initializes new objects(visited, res) to pass
    # depending on state.  
    def stepper(queue, visited=set(), res=[], *args, **kwargs):
        # Catch if queue is a node-type vs a deque queue further in 
        # the stack.  
        if type(queue) != deque:
            queue = deque([queue])
        current = queue.popleft()
        curr_res = func(current, *args, **kwargs)
        res.append(curr_res[1])
        # Try to extend queue with new neighbors checked against 
        # already visited.
        bfs_path(current, queue, visited)
        # To continue 1) Queue must have waiting nodes naturally
        #             2) Function must pass acknowledgement to cont.
        if curr_res[0] == True and len(queue) > 0:
            return stepper(queue, visited, res)
        else:
            return res
    return stepper

def dfs(func):
    def stepper(queue, visited=set(), res=[], *args, **kwargs):
        if type(queue) != deque:
            queue = deque([queue])
        current = queue.popleft()
        curr_res = func(current, *args, **kwargs)
        res.append(curr_res[1])
        dfs_path(current, queue, visited)
        if curr_res[0] == True and len(queue) > 0:
            return stepper(queue, visited, res)
        else:
            return res
    return stepper

# Decorator to catch when the function doesn't return an expected tuple.
def invar(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        if type(results) != tuple:
            return (True, None)
        else:
            return results
    return wrapper


if __name__ == '__main__':

    class Letter():
        def __init__(self, letter):
            self.letter = letter
            self.children = []

    a = Letter('a')
    b = Letter('b')
    c = Letter('c')
    d = Letter('d')
    e = Letter('e')
    f = Letter('f')
    g = Letter('g')
    h = Letter('h')
    a.children = [b, c, f]
    c.children = [d, e]
    f.children = [e, g]
    e.children = [h]
    g.children = [g, h]

    @dfs
    @invar
    def print_(Node):
        print(Node.letter)

    @bfs 
    def set_(Node):
        print(Node.letter)
        Node.alt = Node.letter + 'alt'
        return (True, Node.alt)

    print(print_(a))
    print(set_(a))