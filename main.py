VALID_COMMANDS = 'C,L,U,D'


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


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break

def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def _get_client_field(field_name, message='What is the client {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field

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
    print('[D]elete client')
    print('[S]earch client')


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
    elif command == 'D':
        _show_clients_and_execute_command(delete_client)
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
