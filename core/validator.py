class Validator:

    def validate_docstring(self, docstring):
        issues = []

        if "Parameters:" not in docstring:
            issues.append("Missing Parameters section")

        if "Returns:" not in docstring:
            issues.append("Missing Returns section")

        if len(docstring) < 20:
            issues.append("Docstring too short")

        return issues
