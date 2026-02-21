class Analyzer:
    def __init__(self, parser):
        self.parser = parser

    def detect_issues(self):
        issues = []

        functions = self.parser.get_functions()
        classes = self.parser.get_classes()
        imports = self.parser.get_imports()

        if len(functions) == 0:
            issues.append("No functions found")

        if len(classes) == 0:
            issues.append("No classes found")

        if len(imports) == 0:
            issues.append("No imports found")

        if len(functions) > 10:
            issues.append("Too many functions in file")

        return issues
