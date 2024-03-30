# Inovasys Rule Repository Search Utility

This is a utility tool that allows you to easily take advantage of the [Inovasys Rule Repository](https://addgithublink) by extracting specific rules using the bundles format.

The main function of the tool is to facilitate the following:
1. Listing and filtering available bundles
2. Processing bundles to automatically extract the relevant rules

## Bundles
### What are they?

A bundle in the context of this tool is a way of tying multiple rules together based on a source of data. If theres a yearly threat intel report on the most common attacks conducted, then a bundle would be all the Inovasys rules related to the attacks listed in the report.

### bundle Format

Bundles are yaml based and they contain metadata as well as a list of rules that dictates what rules are relevant to the bundle.

```yaml
title: Short, Descriptive Title
description: A brief description that highlights the aims of the bundle and info about the source reference
category: The bundle category (can currently be Report or CVE)
date: Date when source reference was published (YYYY/MM/DD)
company: Entity that released source reference
reference: Link to source reference
rules: 
    - list of rules (starts from base directory of Inovasys rule repo and links to folder that contains the .yml folder)
    - examples
    - initial_access/initial_access_rule
    - execution/execution_rule_1
    - lateral_movement/lateral_movement_rule
```
## Getting Started
### Installation

The tool has two python files that you can download and run from any directory (both files have to be in the same directory), however the default values for the directory inputs are optimized as if the tool is in the Inovasys rule directory and so it is recommended to place the script there to avoid having to add the directory arguments when running the tool.

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

List all bundles:

```bash
python main.py -l all
```

List bundles for specific category: 

```bash
python main.py -l category_name
```

Process example bundle (default paths):

```bash
python main.py -p example_bundle
```

Process example bundle (custom paths):
```bash
python main.py -p example_bundle -o C:\\path\\to\\output\\dir -r c:\\path\\to\\rules\\dir -c D:\\path\\to\\bundles\\dir
```



