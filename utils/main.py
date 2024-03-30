import argparse
from consumer import Consumer
import os


bundle_categories = ["all", "report", "cve"]
epilog = """
[Example Usage]\n

List all bundles: python main.py -l all\n
List report bundles: python main.py -l report\n
Process example bundle (default paths): python main.py -p example_bundle\n
Process example bundle (custom paths): python main.py -p example_bundle -o C:\\path\\to\\output\\dir -r c:\\path\\to\\rules\\dir -c D:\\path\\to\\bundles\\dir
"""
description = "A tool that allows you to export rules linked in a bundle from the Inovasys sigma rule repo"

parser = argparse.ArgumentParser(
    epilog=epilog,
    description=description,
)

parser.add_argument(
    "-o",
    "--output_dir",
    help="Directory to dump files to",
    default=os.path.join(os.getcwd(), "output"),
)
parser.add_argument(
    "-r", "--rule_dir", help="Directory that contains rules", default=os.getcwd()
)
parser.add_argument(
    "-b",
    "--bundles_dir",
    help="Directory that contains",
    default=os.path.join(os.getcwd(), "bundles"),
)
parser.add_argument(
    "-l",
    "--list_bundles",
    help="List all available bundles",
    choices=bundle_categories,
    default=None,
)
parser.add_argument(
    "-p",
    "--process_bundle",
    help="Bundle to process (dump relevant rules to output directory)",
)

args = parser.parse_args()


if __name__ == "__main__":
    consumer = Consumer(
        rule_dir=args.rule_dir,
        bundles_dir=args.bundles_dir,
        output_dir=args.output_dir,
    )
    if args.list_bundles and args.process_bundle:
        print(
            "List bundle and process bundle cannot be used at the same time, please select one"
        )
        parser.print_help()
    elif args.list_bundles:
        consumer.list_bundles(args.list_bundles)
    elif args.process_bundle:
        consumer.load_bundle(args.process_bundle)
    else:
        print("Please revise entered arguments")
        parser.print_help()
