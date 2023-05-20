import ast
import importlib
import inspect
import networkx as nx
import graphviz
import os
def visualize_dependencies(graph):
    dot = graphviz.Digraph()
    for node in graph.nodes:
        dot.node(node)
    for edge in graph.edges:
        dot.edge(edge[0], edge[1])
    dot.render(view=True)

def get_function_dependencies(file_name, func_name):
    # Import the module from the file
    file_name = file_name.replace('/', '.')
    module_name = os.path.splitext(os.path.basename(file_name))[0]
    package_name = os.path.dirname(file_name).replace(os.path.sep, '.')
    print(package_name)
    print(module_name)
    # module_name = inspect.getmodulename(file_name)
    if module_name is None:
        raise ImportError("Could not find module name for file: " + file_name)
    module = importlib.import_module(module_name, package=package_name)
    
    # Get the function object from the module
    func = getattr(module, func_name, None)
    if func is None:
        raise AttributeError("Function not found: " + func_name)
    
    # Parse the function source code to get the function node
    source_lines, start_lineno = inspect.getsourcelines(func)
    source = "".join(source_lines)
    func_node = ast.parse(source).body[0]
    
    # Build the directed graph of function dependencies
    graph = nx.DiGraph()
    queue = [(func_node, None)]
    while queue:
        node, parent = queue.pop(0)
        if isinstance(node, ast.FunctionDef):
            graph.add_node(node.name)
        if parent is not None:
            graph.add_edge(parent.name, node.name)
        dependencies = get_node_dependencies(node)
        for dep in dependencies:
            dep_obj = getattr(module, dep, None)
            if dep_obj is not None and inspect.isfunction(dep_obj):
                dep_node = ast.parse(inspect.getsource(dep_obj)).body[0]
                queue.append((dep_node, node))
    return graph

def get_node_dependencies(node):
    # Extract the names of the variables used by the node
    if isinstance(node, ast.FunctionDef):
        names = [name.arg for name in node.args.args]
    else:
        names = []
    visitor = DependencyVisitor()
    visitor.visit(node)
    names += visitor.names
    return set(names)

class DependencyVisitor(ast.NodeVisitor):
    def __init__(self):
        self.names = []
    
    def visit_Name(self, node):
        self.names.append(node.id)


if __name__ == "__main__":
    import sys

    func_name,file_name = sys.argv[1:]
    print("Function:", func_name)
    print("File:", file_name)
    graph = get_function_dependencies('/Users/Shuza/Code/PokerAI/poker/train.py', 'train')
    print("Dependencies:")
    # for node in nx.topological_sort(graph):
    #     print(node)
    visualize_dependencies(graph)