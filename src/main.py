# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from FirstQuartile import FirstQuartile
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = XmlDataReader()
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    first_quartile = FirstQuartile(rating).get_first_quartile_students()
    print("First quartile students: ", first_quartile)


if __name__ == "__main__":
    main()
