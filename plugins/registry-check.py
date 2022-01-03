#!/usr/bin/env python

import yaml

registry_filename = 'registry.yaml'

def verify_unique_sources(root: dict):
    if 'plugins' not in root:
        print('plugins entry not found')
        return False
    
    if 'source' not in root['plugins']:
        print('plugins.source entry not found')
        return False
    
    ids = []
    sources = []
    for plugin in root['plugins']['source']:
        id = plugin['id']
        source = plugin['source']
        if id in ids:
            print('verify_unique_sources: id \'{0}\' is not unique'.format(id))
            return False
        if source in sources:
            print('verify_unique_sources: source \'{0}\' is not unique'.format(source))
            return False
        ids.append(plugin['id'])
        sources.append(plugin['source'])
    return True

def main():
    print("Open registry file '{0}'".format(registry_filename))
    with open(registry_filename, "r") as yamlfile:
        try:
            print("Load registry from YAML")
            root = yaml.safe_load(yamlfile)  
            print("Check id and source uniqueness")  
            if not verify_unique_sources(root):
                exit(1)
        except yaml.YAMLError as e:
            print(e)
            exit(1)

if __name__ == "__main__":
    main()