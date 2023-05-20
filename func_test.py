
import inspect

def foo(bob, billy):
    pass

def get_positional_arg_names(func):
    sig = inspect.signature(func)
    return [
        param.name
        for param in sig.parameters.values()
        if param.default == inspect.Parameter.empty and param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
    ]

arg_names = get_positional_arg_names(foo)
print(arg_names)  # Output: ['bob', 'billy']
