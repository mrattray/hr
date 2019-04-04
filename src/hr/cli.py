from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("path", help="path to file")
    parser.add_argument("--export", action="store_true", help="flag for whether this is an export")
    return parser

def main():
    from hr import json, users
    
    args = create_parser().parse_args()
    
    if args.export:
        json.export(args.path)
    else:
         users.sync(json.load(args.path))

