# EDI Utility Scripts

This is a utility tool that allows you to easily take advantage of EDI by extracting specific rules using the bundles format.

The main function of the tool is to facilitate the following:
1. Listing and filtering available bundles
2. Processing bundles to automatically extract the relevant rules

## Bundles
### What are they?

A bundle in the context of this tool is a way of tying multiple rules together based on a source of data. For example, if theres a yearly threat intel report on the most common attacks conducted, then a bundle would be all the rules related to the attacks listed in the report.

### Bundle Format

Bundles are yaml based and they contain metadata as well as a list of rule paths that dictates what rules are relevant to the bundle.

```yaml
title: Short, Descriptive Title
description: A brief description that highlights the aims of the bundle and info about the source reference
category: The bundle category (can currently be Report or CVE)
date: Date when source reference was published (YYYY/MM/DD)
company: Entity that released source reference
reference: Link to source reference
rules: 
    - initial_access/initial_access_rule
    - execution/execution_rule_1
    - lateral_movement/lateral_movement_rule
```

The rules field contatins a list of paths that are mapped to the bundle, the path starts at the base of the repo (tactic name) followed by a forward slash and the name of the rule.

## Getting Started
### Installation

The tool has two python files that you can download and run from any directory (both files have to be in the same directory).

To install the Python library needed for the tool to work:

Windows:

```bash
pip install -r requirements.txt
```

Unix:

```bash
pip3 install -r requirements.txt
```

### Usage

The recommended usage of the script is to run the script from the main EDI directory to avoid having to pass the bundle and rule locations as arguments, however the script can be run from anywhere on the file system as long as the bundle, rule and output locations have been passed as arguments.

List all bundles:

```bash
python utils\bundle_exporter.py -l all
```

List bundles for specific category: 

```bash
python utils\bundle_exporter.py -l category_name
```

Process example bundle (default paths):

```bash
python utils\bundle_exporter.py -p example_bundle
```

Process example bundle (custom paths):
```bash
python utils\bundle_exporter.py -p example_bundle -o C:\path\to\output\dir -r c:\path\to\rules\dir -c D:\path\to\bundles\dir
```



