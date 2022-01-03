#!/usr/bin/env python

from io import TextIOWrapper
import yaml

registry_filename = 'registry.yaml'
doc_filename = 'REGISTRY.md'

def write_source_plugins_table(root: dict, doc: TextIOWrapper):
    if 'plugins' not in root:
        print('plugins entry not found')
        return False
    
    if 'source' not in root['plugins']:
        print('plugins.source entry not found')
        return False
    
    doc.write("## Source plugins\n")
    doc.write("| ID | Event Source | Name | Description | Info\n")
    doc.write("| - | - | - | -- | --\n")
    for plugin in root['plugins']['source']:
        doc.write("| {0} | `{1}` | {2} | {3} | Authors: {4} <br/> Repository: {5} <br/> Contact: {6}\n".format(
            plugin['id'], 
            plugin['source'], 
            plugin['name'], 
            plugin['description'], 
            plugin['authors'], 
            plugin['repository'], 
            plugin['contact'], 
        ))
    return True

def main():
    print("Open registry file '{0}'".format(registry_filename))
    with open(registry_filename, "r") as yamlfile:
        try:
            print("Load registry from YAML")
            root = yaml.safe_load(yamlfile)  
            print("Generate md doc")  
            with open(doc_filename, "w") as docfile:
                if not write_source_plugins_table(root, docfile):
                    exit(1)
        except yaml.YAMLError as e:
            print(e)
            exit(1)

if __name__ == "__main__":
    main()