import sys
from core.parser import CodeParser
from core.analyzer import Analyzer
from core.docstring_generator import DocstringGenerator
from core.validator import Validator
from core.metrics import Metrics
from core.report import ReportGenerator


def run_review(filepath):
    parser = CodeParser(filepath)
    analyzer = Analyzer(parser)
    docgen = DocstringGenerator()
    validator = Validator()
    metrics = Metrics()
    reporter = ReportGenerator()

    report_data = []

    print("\n--- Code Review Report ---\n")

    print("Functions:", parser.get_functions())
    print("Classes:", parser.get_classes())
    print("Imports:", parser.get_imports())

    issues = analyzer.detect_issues()
    print("\nCode Issues:", issues)

    print("\nDocstring Analysis:")

    for func in parser.get_functions():
        doc = docgen.generate(func)
        problems = validator.validate_docstring(doc)
        score = metrics.calculate_score(problems)

        print(f"\nFunction: {func}")
        print(doc)
        print("Validation Issues:", problems)
        print("Quality Score:", score)

        # save for csv report
        report_data.append([func, score, ",".join(problems)])

    # save csv report
    reporter.save_report("reports/report.csv", report_data)
    print("\nReport saved to reports/report.csv")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m cli.main <python_file>")
    else:
        run_review(sys.argv[1])
