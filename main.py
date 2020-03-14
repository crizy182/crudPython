VALID_COMMANDS = 'C,L,U'


clients = 'tomas,juan,'


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already in client\'s list')


def list_clients():
    print(clients)


def update_client():
    client_name = _get_client_name()
    updated_name = input('What is the new client name? ')
    _update_client(client_name, updated_name)


def _update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        print('Client not in client\'s list')

def _add_comma():
    global clients

    clients += ','

def _get_client_name():
    return input('What is the client name?')


def _print_line():
    print('*' * 50)


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    _print_line()
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')


def _show_clients_and_execute_command(command):
    print('Current clients:')
    print('')
    list_clients()
    _print_line()

    command()

    print('')
    _print_line()
    print('Updated clients:')
    list_clients()


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        _show_clients_and_execute_command(update_client)

    else:
        print('Invalid command')