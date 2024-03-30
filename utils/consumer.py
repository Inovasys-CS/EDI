import yaml, os, shutil


class Consumer:
    def __init__(
        self,
        rule_dir: str = "rules",
        bundles_dir: str = "bundles",
        output_dir: str = "output",
    ) -> None:
        self.rule_dir = rule_dir
        self.bundles_dir = bundles_dir
        self.output_dir = output_dir

    def load_bundle(self, wanted_bundle: str) -> bool:
        """Extracts rules list from bundle yaml"""

        try:
            bundles = os.listdir(self.bundles_dir)
            bundles = [bundle for bundle in bundles if bundle.endswith(".yml")]
        except FileNotFoundError:
            print("Bundles folder does not exist")
            exit()
        contains = []
        for bundle in bundles:
            if wanted_bundle in bundle:
                contains.append(bundle)

        # Check to ensure that there aren't more than one match to the bundle name
        if len(contains) > 1:
            print(
                "More than one bundle have the same name, please enter a more specific bundle name"
            )
            print(contains)
            return False
        elif len(contains) == 0:
            print("Bundle not found")
            return False
        else:
            # Read file and parse raw yaml file to dictionary object, extracting from it the rules list
            raw_file = open(os.path.join(self.bundles_dir, bundle)).read()
            rules = yaml.load(raw_file, Loader=yaml.Loader)["rules"]
            self.export_bundle(rules)
            return True

    def export_bundle(self, rules: list) -> None:
        """Copies rules indicated in rule list to output directory"""

        not_found = []
        for rule in rules:
            # Combines rule name with rule directory to be used in file copy function
            rule_path = os.path.join(
                self.rule_dir, rule if os.name == "posix" else rule.replace("/", "\\")
            )
            try:
                dir_content = os.listdir(rule_path)
            except FileNotFoundError:
                not_found.append(rule)
                if len(not_found) == len(rules):
                    print(
                        "None of the specified rules were found, check rules directory path"
                    )
                    exit()
                continue

            # Copies all rules related to use case
            if os.path.isdir(self.output_dir):
                for item in dir_content:
                    if item.endswith(".yml"):
                        shutil.copy2(os.path.join(rule_path, item), self.output_dir)
            else:
                print("Output directory does not exist")
                exit()

        # Display completion status
        print(
            f"Export status: {len(rules) - len(not_found)} Successful, {len(not_found)} Failed, {len(rules)} Total"
        )
        if not_found:

            print("\nFailed rules: ")
            for rule in not_found:
                print(f"- {rule}")

    def list_bundles(self, target: str = "all") -> None:
        """Lists all bundles or bundles with specific category based on user input"""

        bundles = os.listdir(self.bundles_dir)
        for bundle in bundles:
            bundle_name = bundle.replace(".yml", "")

            # Load and parse yaml file
            raw_file = open(self.bundles_dir + "\\" + bundle).read()
            yaml_parsed = yaml.load(raw_file, Loader=yaml.Loader)

            # Check whether the bundle's category matches desired category
            if target == "all":
                self.print_bundle(yaml_parsed, bundle_name)
            elif target == yaml_parsed["category"].lower():
                self.print_bundle(yaml_parsed, bundle_name)
            else:
                continue

    def print_bundle(self, yaml_parsed: dict, bundle_name: str) -> None:
        """Prints bundle infortmation"""

        print(f"Bundle: {yaml_parsed['title']} ({bundle_name})")
        print(f"Description: {yaml_parsed['description']}")
        print(f"Category: {yaml_parsed['category']}")
        print(f"Date: {yaml_parsed['date']}")
        print(f"Number of rules: {len(yaml_parsed['rules'])}")
        print("=" * 50)
