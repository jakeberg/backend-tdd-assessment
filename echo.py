import sys
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    
    parser.add_argument("-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument("-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument("-t", "--title", help="convert text to titlecase", action="store_true")
    parser.add_argument("text", help="text to be manipulated" )

    return parser

def main(args):

    parser = create_parser()

    # Checks to see if args are present and sends usage if there are not
    if not args:
        parser.print_usage()
        sys.exit()

    args = parser.parse_args(args)
    
    text = args.text

    # Performs operations if they are in args
    if args.upper:
        text = text.upper()
    if args.lower: 
        text = text.lower()
    if args.title:
        text = text.title()

    return text


if __name__ == "__main__":
    print main(sys.argv[1:])
