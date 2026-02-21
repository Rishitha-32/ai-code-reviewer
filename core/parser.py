import ast

class CodeParser:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as f:
            self.tree = ast.parse(f.read())

    def get_functions(self):
        return [
            node.name
            for node in ast.walk(self.tree)
            if isinstance(node, ast.FunctionDef)
        ]

    def get_classes(self):
        return [
            node.name
            for node in ast.walk(self.tree)
            if isinstance(node, ast.ClassDef)
        ]

    def get_imports(self):
        imports = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for name in node.names:
                    imports.append(name.name)
        return imports
