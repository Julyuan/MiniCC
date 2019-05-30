import calcyacc

s = '''int main(void){int a;return 0;}'''
res = calcyacc.parse_grammar(s)
print(res)
symbol_table_keyword = ('program','functionDeclaration','compoundStatement')
parent_node = {}
parent_node[0] = -1
symbol_table_id = {}

def find_parent():
    pass
def merge_table():
    pass
def create_symbol_table(node_id):
    return 0

counter = 0
def preorder_traverse(tree):
    global counter
    global symbol_table_id
    node_id = counter
    counter += 1
    print(node_id,' ',tree)
    if hasattr(tree,'__len__') and tree[0] in symbol_table_keyword:
        symbol_table_id[node_id] = create_symboltable(node_id)
    if tree is None or type(tree) == int or type(tree)==float or type(tree)==str:
        print(tree)
    elif type(tree)==list:
        for i in tree:
            parent_node[preorder_traverse(i)] = node_id
    # elif len(tree)==1 and (type(tree[1])==str or type(tree[1])==int or type(tree[1])==float):
    else:
        print(tree[0])
        for i in tree[1:]:
            parent_node[preorder_traverse(i)] = node_id
    return node_id

preorder_traverse(res)

for i in parent_node.keys():
    print('parent node of',i,'is',parent_node[i])

class symbol_table(object):
    def __init__(self,id):
        self.table = {}
        self.id = id
    def add_declaration(self, pos, identifier):
        if self.table.get(identifier) == -1:
            self.table[identifier] = pos
        else:
            pass