from graphviz import Digraph

def show_syntax_tree(tuple_tree, save_path, viewnow=False):
    plot_model(tree2dict(buildtree(tuple_tree)), save_path, viewnow)


# root1 = ('program', ('declarationList', [('declaration', ('staticVariableDeclaration', ('typeSpec', 'int'), ('declaratorList', [('declarator', 'i')]))), ('declaration', ('functionDeclaration', ('typeSpec', 'int'), 'main', ('parameters', 'void'), ('compoundStatement', ('optionalLocalDeclarations', ('localDeclarations', [('localDeclaration', ('staticVariableDeclaration', ('typeSpec', 'int'), ('declaratorList', [('declarator', 'a'), ('declarator', 'b')])))])), ('optionalStatementList', ('statementList', [('statement', ('expressionStatement', ('assignExpression', ('identifier-expression', 'a'), ('int-expression', 0)))), ('statement', ('expressionStatement', ('assignExpression', ('identifier-expression', 'b'), ('int-expression', 2)))), ('statement', ('expressionStatement', ('assignExpression', ('identifier-expression', 'i'), ('int-expression', 0)))), ('statement', ('whileStatement', ('binary-expression', '<', ('identifier-expression', 'i'), ('int-expression', 10)), ('statement', ('compoundStatement', ('optionalLocalDeclarations', None), ('optionalStatementList', ('statementList', [('statement', ('expressionStatement', ('assignExpression', ('identifier-expression', 'a'), ('binary-expression', '+', ('identifier-expression', 'a'), ('identifier-expression', 'b'))))), ('statement', ('expressionStatement', ('assignExpression', ('identifier-expression', 'i'), ('binary-expression', '+', ('identifier-expression', 'i'), ('int-expression', 1)))))])))))), ('statement', ('expressionStatement', ('functioncallExpression', 'printf', ('argumentExpressionList', [('stringExpression', '"%d\\n"'), ('identifier-expression', 'a')])))), ('statement', ('returnStatement', ('int-expression', 0)))])))))]))


class Node:
    def __init__(self, c=[], v=None):
        self.children = c
        self.value = v


def buildtree(root):
    if type(root)!=tuple:
        return Node([], root)
    node = Node([], root[0])
    if type(root[1]) == list:
        for x in root[1]:
            node.children.append(buildtree(x))
    else:
        for i in range(1, len(root)):
            node.children.append(buildtree(root[i]))
    return node

# r = buildtree(root1)

def visit(tree):
    print(tree.value)
    for c in tree.children:
        visit(c)

def tree2dict(root):
    if len(root.children)==0:
        return str(root.value)
    res = {root.value: {}}
    cnt = 0
    for c in root.children:
        res[root.value].setdefault(cnt, tree2dict(c))
        cnt+=1
    return res

# tmp = tree2dict(r)
# print(tmp)

######################################################
def plot_model(tree, name, viewnow=False):
    g = Digraph("G", filename=name, format='png', strict=False)
    first_label = list(tree.keys())[0]
    g.node("0", first_label)
    _sub_plot(g, tree, "0")
    if viewnow:
        g.view()


root = "0"

def _sub_plot(g, tree, inc):
    global root

    first_label = list(tree.keys())[0]
    ts = tree[first_label]
    for i in ts.keys():
        if isinstance(tree[first_label][i], dict):
            root = str(int(root) + 1)
            g.node(root, list(tree[first_label][i].keys())[0])
            g.edge(inc, root, str(i))
            _sub_plot(g, tree[first_label][i], root)
        else:
            root = str(int(root) + 1)
            g.node(root, tree[first_label][i])
            g.edge(inc, root, str(i))


if __name__=='__main__':
    d1 = {"no surfacing": {0: "no", 1: {"flippers": {0: "no", 1: "yes"}}}}

    d2 = {'tearRate': {'reduced': 'no lenses', 'normal': {'astigmatic': {'yes': {
        'prescript': {'myope': 'hard', 'hyper': {'age': {'young': 'hard', 'presbyopic': 'no lenses', 'pre': 'no lenses'}}}},
        'no': {'age': {'young': 'soft', 'presbyopic': {
            'prescript': {'myope': 'no lenses',
                        'hyper': 'soft'}},
                    'pre': 'soft'}}}}}}

    plot_model(d1, "d1.gv")
    # plot_model(d2, "hello2.gv")
