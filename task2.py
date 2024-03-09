def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        add_contact(args, contacts)
        return "contact added"
    
    return "contact not found"
    
def show_phone(args, contacts):
    name = args
    if name[0] in contacts.keys():
        return contacts[name[0]]
        
    return "Contact not found"

def show_all(args, contacts):
    for name in contacts:
        yield f"{name} {contacts[name]}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        commands = {
            "add" : add_contact,
            "change": change_contact,
            "phone": show_phone,
        }
        
        if command == "hello":
            print("How can I help you?")
        elif command == "all":
            for line in show_all(args, contacts):
                print(line)
        elif command in commands:
            print(commands[command](args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

