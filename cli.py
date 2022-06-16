import argparse
import sys

description = 'Generate MCQs from text using Natural Language Processing'
parser = argparse.ArgumentParser(description=description)

parser.add_argument('input',
                    type=argparse.FileType('r'),
                    metavar="Input File",
                    help='The file will be used as input'
                    )

parser.add_argument(
    '--output', '-o',
    default=sys.stdout,
    metavar="Output File",
    type=argparse.FileType('w'),
    help="This file will be used as output")
