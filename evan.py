class EvanEnum():
    def __init__(self, s):
        vals = s.split()
        self.val_to_index = {k: i for i, k in enumerate(vals)}
        self.index_to_val = {i: k for i, k in enumerate(vals)}

def make_enum(s):
    vals = s.split()
    print(vals)

e = EvanEnum("""
    george dave sam
    pie apples carrot
    happy sad
""")

print(e.val_to_index['sad'])

# vals = [
#     'george',
#     'dave',
#     'pie',
#     'apples',
# ]

# v = {k: i for i, k in enumerate(vals)}
# a= [0,2,5,3,4]

# a.append(v['george'])


# def foo(george, dave, pie, apples):

#     pass

# make_arg_enum(george=1, dave=2)


# import inspect
# import ast

# def print_param_names():
#     frame = inspect.currentframe()
#     tree = ast.parse(inspect.getsource(frame.f_code))

#     param_names = []
#     for node in ast.walk(tree):
#         if isinstance(node, ast.FunctionDef) and node.name == frame.f_code.co_name:
#             for arg in node.args.args:
#                 param_names.append(arg.arg)

#     print("Parameter names:", ", ".join(param_names))
