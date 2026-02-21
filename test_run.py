from core.parser import CodeParser
from core.analyzer import Analyzer
from core.docstring_generator import DocstringGenerator
from core.validator import Validator
from core.metrics import Metrics

parser = CodeParser("sample.py")
analyzer = Analyzer(parser)
docgen = DocstringGenerator()
validator = Validator()
metrics = Metrics()

print("Functions:", parser.get_functions())
print("Classes:", parser.get_classes())
print("Imports:", parser.get_imports())
print("Issues:", analyzer.detect_issues())

print("\nDocstring Analysis:")

for func in parser.get_functions():
    doc = docgen.generate(func)
    problems = validator.validate_docstring(doc)
    score = metrics.calculate_score(problems)

    print(f"\nFunction: {func}")
    print(doc)
    print("Validation Issues:", problems)
    print("Quality Score:", score)
