import argparse
import functions


parser = argparse.ArgumentParser(description="My hw7 APP")
parser.add_argument('--action', help='Command: create, update, list, remove')
parser.add_argument('--model', help='Command: StuGroup, Student, Teacher, Subject, Grade')
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--name')
parser.add_argument('--group_number')
parser.add_argument('--number_grade')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('actin')
model = my_arg.get('model')
id = my_arg.get('id')
title = my_arg.get('title')
name = my_arg.get('name')
group_number = my_arg.get('group_number')
number_grade = my_arg.get('number_grade')


def main():
    match model:
        case 'StuGroup':
            match action:
                case 'create':
                    functions.create_group(group_number)
                case 'list':
                    functions.read_group()
                case 'update':
                    functions.update_group(id, group_number)
                case 'remove':
                    functions.delete_group(id)
        case 'Student':
            match action:
                case 'create':
                    functions.create_student(name)
                case 'list':
                    functions.read_student()
                case 'update':
                    functions.update_student(id, name)
                case 'remove':
                    functions.delete_student(id)
        case 'Teacher':
            match action:
                case 'create':
                    functions.create_teacher(name)
                case 'list':
                    functions.read_teacher()
                case 'update':
                    functions.update_teacher(id, name)
                case 'remove':
                    functions.delete_teatcher(id)
        case 'Subject':
            match action:
                case 'create':
                    functions.create_subject(title)
                case 'list':
                    functions.read_subject()
                case 'update':
                    functions.update_subject(id, title)
                case 'remove':
                    functions.delete_subject(id)
        case 'Grade':
            match action:
                case 'create':
                    functions.create_grade(number_grade)
                case 'list':
                    functions.read_grade()
                case 'update':
                    functions.update_grade(id, number_grade)
                case 'remove':
                    functions.delete_grade(id)

if __name__=="__main__":
    main()
