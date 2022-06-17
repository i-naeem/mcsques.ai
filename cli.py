import argparse
import sys

description = 'Generate MCQs from text using Natural Language Processing'
parser = argparse.ArgumentParser(description=description)

parser.add_argument('input',
                    type=argparse.FileType(mode='r', encoding='UTF-8'),
                    metavar="Input File",
                    help='The file will be used as input'
                    )

parser.add_argument(
    '--output', '-o',
    default=sys.stdout,
    metavar="Output File",
    type=argparse.FileType(mode='w', encoding='UTF-8'),
    help="This file will be used as output")

args = parser.parse_args()
