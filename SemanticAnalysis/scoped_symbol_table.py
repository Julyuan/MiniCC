def show_symbol_table(st):
    lines = []
    functions = list(st.keys())
    functions.remove('global')
    for key in st:
        if key != 'global':
            scope_name = key
            scope_level = 1
            enclosing_scope_name = 'global'
            items = []
            for x in (st[key]['local_para'] + st[key]['local_var']):
                items.append((x[1], x[0]))
            lines.append(func(scope_name, scope_level, enclosing_scope_name, items))
        else:
            scope_name = key
            scope_level = 0
            enclosing_scope_name = None
            items = []
            for x in (st[key]['global_var']):
                items.append((x[1], x[0]))
            for x in functions:
                items.append((x, 'function'))
            lines.append(func(scope_name, scope_level, enclosing_scope_name, items))
    s = '\n'.join(lines)
    return s


def func(scope_name, scope_level, enclosing_scope_name, items):
    h1 = 'Scoped Symbol Table'
    lines = ['\n', h1, '=' * len(h1)]
    for header_name, header_value in (
        ('Scope name', scope_name),
        ('Scope level', scope_level),
        ('Enclosing scope', enclosing_scope_name),
    ):
        lines.append('%-15s: %s' % (header_name, header_value))
    h2 = 'Contents'
    lines.extend([h2, '-' * len(h2)])
    lines.extend(
        ('%7s: %r' % (key, value))
        for key, value in items
    )
    lines.append('\n')
    s = '\n'.join(lines)
    return s


if __name__ =='__main__':
    st={'go': {'local_para': [('int', 'a', (False, 1), 0)], 'local_var': [('int', 'g', (False, 1), -4)]}, 'main': {'local_para': [], 'local_var': []}, 'global': {'global_var': [('int', 'i', (False, 1), None), ('char', 'aDN', (True, None), b'"%d\\n"')]}}
    print(show_symbol_table(st))
