from ..main import inttrav

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
graph = [a, b, c, d, e, f, g, h]

@dfs 
def travel(Node):
    print(Node.letter)
    return True

if __name__ == '__main__':
    travel(a)