import os
import yaml

def convert_to_md(yaml_file, output_dir):
    with open(yaml_file, 'r') as file:
        yaml_parsed = yaml.safe_load(file)
    
    rules = ""
    root_dir = "https://github.com/Inovasys-CS/EDI/tree/main/"
    for i, rule in enumerate(yaml_parsed["rules"], 1):
        rules += f"{i}. [{rule}]({root_dir + rule})\n"

    md_content = f"""
# {yaml_parsed['title']}

{yaml_parsed['company']} - {yaml_parsed['date']}, {yaml_parsed['category']}, [Reference Link]({yaml_parsed['reference'].split('?')[0]})

{yaml_parsed['description']}

## Related Rules

{rules}
"""
    md_name = yaml_file.split("/")[-1].replace(".yml", ".md")
    md_path = os.path.join(output_dir, md_name)
    if not os.path.exists(md_path):
        with open(md_path, "w") as md_file:
            md_file.write(md_content)
        print(f"Markdown file created: {md_path}")
    else:
        print(f"Markdown file already exists: {md_path}")

def main():
    output_dir = 'bundles'
    for filename in os.listdir(output_dir):
        if filename.endswith('.yml'):
            yaml_path = os.path.join(output_dir, filename)
            convert_to_md(yaml_path, output_dir)

if __name__ == "__main__":
    main()
