def main():
    phone_dictionary = {} #initialize new dictionary again

    name = ''
    phone = ''
    accept_input = True
    while accept_input:
        print('Enter phone book name: Or done.')
        name = input()
        print('Enter phone book number associated with that name: ')
        phone = input()
        if not(name in phone_dictionary):
            phone_dictionary[name] = phone

    print('Enter \'n\' to lookup the phone book by name or \'p\' by phone number:')
    input_choice = input()
    if 'n' == input_choice:
         print('Enter the name to lookup:')
         name = input()
         print('Found name', name, 'with phone number', phone_dictionary[name])
    elif 'p' == input_choice:
         print('Enter the phone number to lookup:')
         phone = input()
         for name in phone_dictionary:
             if phone == phone_dictionary[name]:
                 print('Found phone number', phone,'associated name', name)
                 break

if __name__ == "__main__":
    sys.exit(int(main() or 0))