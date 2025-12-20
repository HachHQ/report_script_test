import argparse
import sys
from tabulate import tabulate

from src.loader import load_data
from src.reports import get_report_generator

def parse_arguments():
    parser = argparse.ArgumentParser(prog="reporter",
                                    description="Get csv files and table argument.")
    parser.add_argument("--files", "-f", nargs="+", required=True, help="Path to input csv file.", default=None)
    parser.add_argument("--report", "-r", required=True, help="Argument of table in csv.", default=None)
    return parser.parse_args()


def main():
    args = parse_arguments()

    try:
        data = load_data(args.files)
        if not data:
            print("No data found in provided files.")
            sys.exit(0)

        report_generator = get_report_generator(args.report)

        report_data = report_generator.generate(data)

        rows = [[row[h.lower().replace(" ", "_")] for h in report_generator.headers] for row in report_data]

        print(tabulate(rows, headers=report_generator.headers, tablefmt="rounded_outline"))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()