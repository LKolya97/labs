def depth(tree, k):
    d = 0
    while (tree[k]):
       
            k = tree[k]
            d+=1
    
    return d

f = open('RodTree.txt') 
line = f.readline()
n = int (line)
tree = {}
for i in range(n):
    line = f.readline()
    while line:
        child, parent = line.split()
        tree[child] = parent
        if not parent in tree:
            tree[parent]=None
        line = f.readline()
for k,v in sorted(tree.items()):
    print(k, depth(tree, k))
