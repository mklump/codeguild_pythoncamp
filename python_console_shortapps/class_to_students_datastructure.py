
def main():
    class_name_to_students = dict()  #initialized empty dictionary

    accept_input = True
    while accept_input:
        print('Student name? Or done.')
        student_name = input()
        accept_input = student_name != 'done'
        if accept_input:
            print('What class is ' + student_name + ' in?')
            class_name = input()

            if class_name in class_name_to_students:
                old_roster = class_name_to_students[class_name]
            else:
                old_roster = set()
            new_roster = old_roster | {student_name}
            class_name_to_students[class_name] = new_roster

    print(class_name_to_students)

if __name__ == "__main__":
    sys.exit(int(main() or 0))