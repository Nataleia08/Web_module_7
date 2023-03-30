import argparse
import functions


parser = argparse.ArgumentParser(description="My hw7 APP")
parser.add_argument('--action', help='Command: create, update, list, remove')
parser.add_argument('--model', help='Command: StuGroup, Student, Teacher, Subject, Grade')
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--name')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('actin')
model = my_arg.get('model')
id = my_arg.get('id')
title = my_arg.get('title')
name = my_arg.get('name')


def main():
    

if __name__=="__main__":
    main()
