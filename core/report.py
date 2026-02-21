import csv

class ReportGenerator:

    def save_report(self, filename, data):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Function", "Score", "Issues"])

            for row in data:
                writer.writerow(row)
