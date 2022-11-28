import graphviz as gv


def draw_graph(vertices, names, edges):
    g = gv.Digraph('graph',
                   engine='neato',
                   graph_attr=dict(splines='true',
                                   overlap='scale'),
                   node_attr=dict(shape='plaintext',
                                  margin='0',
                                  fontsize='10', ),
                   edge_attr=dict(arrowsize='0.4'))
    g.engine = 'circo'
    for v in vertices:
        g.node(str(v), label=names[v])
    for e in edges:
        g.edge(str(e[0]), str(e[1]))
    print("viewing")
    g.view()
