from collections import UserDict




# name = Name("Assica")
# phone = Phone("69 69 69")

# record1 = Record(name, phone)
# record1.add_phone_number(Phone("34563456"))
# record1.add_phone_number(Phone("23465785"))
# record1.add_phone_number(Phone("234535678453245"))
# record1.add_phone_number(Phone("234556785"))

# record2 = Record(Name("Sexica"), Phone("69"), Phone("11111"), Phone("2222222"))


# #print(record1.name, [number.value for number in record1.phone_numbers]) #_numbers
# print(record2.name, *record2.phone_numbers)
























# phonebook = {}

# def command_error(func):
#     def inner(*args):
#         try:
#             return func(*args)
#         except KeyError:
#             return 'Unknown command, type "help" to see the list of commands'
#         except IndexError:
#             return 'Not enough arguments'
#     return inner

# def greeting(args):
#     return "How can I help you?"

# def help(args):
#     commands = [{"command": "hello", "description": "show greeting"},
#                 {"command": "help", "description": "show all available commands"},
#                 {"command": "add, name, phone_number", "description": "add a new contact"},
#                 {"command": "change, name, new_phone_number", "description": "change the phone number of an existing contact"},
#                 {"command": "phone, name", "description": "show the phone number of a contact"},
#                 {"command": "show all", "description": "show all contacts in console"},
#                 {"command": "goodbye", "description": "exit Phonebook manager"},
#                 {"command": "close", "description": "exit Phonebook manager"},
#                 {"command": "exit", "description": "exit Phonebook manager"}]
#     result = ""
#     for item in commands:
#         result += f'{item["command"]}: {item["description"]}\n'
#     return result

# def parcer(user_input):
#     user_input += ","
#     disected_input = user_input.lower().split(",")
#     disected_input.remove('')
#     results = list()
#     for i in disected_input:
#         results.append(i.lower().strip(' '))
#     return results

# def add(args):
#     if args[0] in phonebook.keys():
#         return "A contact with this name already exists"
#     phonebook[args[0]] = args[1]
#     return f"Contact added: {args[0].capitalize()}: {args[1]}"

# def change(args):
#     if args[1] in phonebook.keys():
#         phonebook[args[1]] = args[2]
#         return f"Contact changed to {args[1].capitalize()}: {args[2]}"
#     return 'Contact not found'

# def show_contact(args):
#     if args[0] in phonebook.keys():
#         return f"{args[0].capitalize()}: {phonebook[args[0]]}"  
#     return f"{args[0].capitalize()} not found"

# def show_all(args):
#     result = ""
#     for name, phone_number in phonebook.items():
#         result += f"{name.capitalize()}: {phone_number}\n"     
#     return result

# @command_error
# def handler(command, args):
#     functions = {
#                 "hello": greeting,
#                 "help": help,
#                 "add": add,
#                 "change": change,
#                 "phone": show_contact,
#                 "show all": show_all 
#                 }
#     return functions[command](args)

# def main():
#     print("Greetings, user! Phonebook manager online")
#     while True:
#         user_input = parcer(input('Enter a command: \n>>> '))
#         command = user_input[0]
#         user_input.remove(command)
#         args = [arg for arg in user_input]
#         #print(user_input)
#         if command in ("goodbye", "close", "exit"):
#             print("Goodbye!")
#             break
#         result = handler(command, args)
#         if result == "":
#             result = "Seems like your list of contacts is empty. Try adding some" 
#         print(result)

# main()


















class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    pass


class Phone(Field):

    pass


class Addressbook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:

    def __init__(self, name:Name, *phone_numbers:Phone):
        self.name = name
        #self.phone = phone_number
        self.phone_numbers = []
        if phone_numbers:
            for i in phone_numbers:
                self.phone_numbers.append(i)

    def add_phone_number(self, phone_number:Phone):
        if phone_number not in self.phone_numbers:
            self.phone_numbers.append(phone_number)
            return f"Phone number {phone_number.value} was added to {self.name.value.capitalize()}"
        else:
            return f"Phone number {phone_number.value} already exists in{self.name.value.capitalize()}"

    def remove_phone_number(self, phone_number:Phone):
        if phone_number in self.phone_numbers:
            self.phone_numbers.remove(phone_number)
            return f"Phone number {phone_number.value} was removed from {self.name.value.capitalize()}"
        else:
            return f"Phone number {phone_number.value} was not found in {self.name.value.capitalize()}"

    def edit_phone_number(self, new_number:Phone, old_number:Phone=None):
            self.remove_phone_number(old_number)
            self.add_phone_number(new_number)







# addressbook = Addressbook()

# record1 = Record(Name("assica"), Phone("69 69 69"), Phone("+69"))

# addressbook.add_record(record1)

# print(addressbook[record1.name.value].name.value)

# if "assica" in addressbook.data.keys():
#     print("it works")



















#phonebook = {}
addressbook = Addressbook()

def command_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Unknown command, type "help" to see the list of commands'
        except IndexError:
            return 'Not enough arguments'
        except TypeError:
            return 'Missing some arguments'
    return inner

def greeting(*args):
    return "How can I help you?"

def help(*args):
    commands = [{"command": "hello", "description": "show greeting"},
                {"command": "help", "description": "show all available commands"},
                {"command": "add, name, phone_number", "description": "add a new contact"},
                {"command": "change, name, new_phone_number", "description": "change the phone number of an existing contact"},
                {"command": "phone, name", "description": "show the phone number of a contact"},
                {"command": "show all", "description": "show all contacts in console"},
                {"command": "goodbye", "description": "exit Phonebook manager"},
                {"command": "close", "description": "exit Phonebook manager"},
                {"command": "exit", "description": "exit Phonebook manager"}]
    result = ""
    for item in commands:
        result += f'{item["command"]}: {item["description"]}\n'
    return result

def parcer(user_input):
    user_input += ","
    disected_input = user_input.lower().split(",")
    disected_input.remove('')
    results = list()
    for i in disected_input:
        results.append(i.lower().strip(' '))
    return results

def add(name, *args):
    #print(args)
    if name in addressbook.data.keys():
        result = str()
        for arg in args:            
            result += addressbook.data[name].add_phone_number(Phone(arg)) + "\n"
        return result
    name = Name(name)
    phones = [Phone(p) for p in args]
    record = Record(name, *phones)
    addressbook.add_record(record)
    return f"Contact added: {name.value.capitalize()}: {[phone.value for phone in phones]}"

def change(name, *args):
    if name in addressbook.data.keys():
        addressbook.data[name].phone_numbers = [Phone(p) for p in args]
        return f"Contact changed to {name.capitalize()}: {[(p) for p in args]}"
    return 'Contact not found'

def change_phone(name, old_phone, *new_phones):
    pass

def remove_phone(name, phone, *args):
    pass

def show_contact(*names):
    result_found = ""
    result_not = ""
    for name in names:
        if name in addressbook.data.keys():
            result_found += f"---------------------------------------------------------\n{name.capitalize()}:\n"
            for phone in addressbook.data[name].phone_numbers:
                result_found += f"{phone.value}\n"
        else: result_not += f"---------------------------------------------------------\n{name} not found\n"
    return f"{result_found}{result_not}"

def show_all(*args):
    result = ""
    for name, record in addressbook.data.items():
        result += f"---------------------------------------------------------\n{name.capitalize()}:\n"
        for phone in record.phone_numbers:
            result += f"{phone.value}\n"
        #result += f"\n"     
    return result

@command_error
def handler(command, args):
    functions = {
                "hello": greeting,
                "help": help,
                "add": add,
                "change": change,
                # "change phone": change_phone,
                # "remove phone": remove_phone,
                "phone": show_contact,
                "show all": show_all 
                }
    #print(f"function: {command}{args}")
    return functions[command](*args)

def main():
    print("Greetings, user! Phonebook manager online")
    while True:
        user_input = parcer(input('Enter a command: \n>>> '))
        command = user_input[0]
        user_input.remove(command)
        args = [arg for arg in user_input]
        #print(user_input)
        if command in ("goodbye", "close", "exit"):
            print("Goodbye!")
            break
        result = handler(command, args)
        if result == "":
            result = "Seems like your list of contacts is empty. Try adding some" 
        print(result)

main()