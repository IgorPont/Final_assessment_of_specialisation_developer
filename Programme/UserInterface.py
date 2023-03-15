def ls_menu():
    print('\nWelcome to the pet register!')

    while True:
        print('\nSelect the menu item by entering the appropriate number:\n'
              '1. View the animal register\n'
              '2. Get a new pet\n'
              '3. Actions with animals\n'
              '4. Exit\n')

        user_input = input('Enter: ')
        if user_input.isdigit():
            match int(user_input):
                case 1:
                    while True:
                        print('\nSelect the menu item by entering the appropriate number:\n'
                              '1. Domestic animals\n'
                              '2. Pack animals\n'
                              '3. Go back\n')

                        user_input = input('Enter: ')
                        if user_input.isdigit():
                            match int(user_input):
                                case 1:
                                    while True:
                                        print('\nSelect the menu item by entering the appropriate number:\n'
                                              '1. Dogs\n'
                                              '2. Cats\n'
                                              '3. Hamsters\n'
                                              '4. Go back\n')

                                        user_input = input('Enter: ')
                                        if user_input.isdigit():
                                            match int(user_input):
                                                case 1:
                                                    pass
                                                case 2:
                                                    pass
                                                case 3:
                                                    pass
                                                case 4:
                                                    break
                                        else:
                                            print('\nYou entered the wrong number. Try again.')
                                case 2:
                                    while True:
                                        print('\nSelect the menu item by entering the appropriate number:\n'
                                              '1. Horses\n'
                                              '2. Camels\n'
                                              '3. Donkeys\n'
                                              '4. Go back\n')

                                        user_input = input('Enter: ')
                                        if user_input.isdigit():
                                            match int(user_input):
                                                case 1:
                                                    pass
                                                case 2:
                                                    pass
                                                case 3:
                                                    pass
                                                case 4:
                                                    break
                                        else:
                                            print('\nYou entered the wrong number. Try again.')
                                case 3:
                                    break
                        else:
                            print('\nYou entered the wrong number. Try again.')
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    print('\nGoodbye!')
                    break
                case _:
                    print(f"\nSorry, I couldn't understand {user_input}.")
        else:
            print('\nYou entered the wrong number. Try again.')
