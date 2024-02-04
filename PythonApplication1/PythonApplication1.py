def read_phonebook(filename="phonebook.txt"):
    """������ ���������� ���������� �� �����."""
    with open(filename, "a+"):
        pass

    with open(filename, "r") as file:
        lines = file.readlines()

    phonebook = {}
    for line in lines:
        surname, name, phone = line.strip().split(";")
        phonebook[surname] = (name, phone)
    return phonebook


def write_phonebook(phonebook, filename="phonebook.txt"):
    """���������� ���������� ���������� � ����."""
    with open(filename, "w") as file:
        for surname, (name, phone) in phonebook.items():
            file.write(f"{surname};{name};{phone}\n")


def add_entry(surname, name, phone):
    phonebook = read_phonebook()
    phonebook[surname] = (name, phone)
    write_phonebook(phonebook)


def update_entry(surname, name=None, phone=None):
    phonebook = read_phonebook()
    if surname in phonebook:
        current_name, current_phone = phonebook[surname]
        phonebook[surname] = (name if name else current_name, phone if phone else current_phone)
        write_phonebook(phonebook)


def delete_entry(surname):
    phonebook = read_phonebook()
    if surname in phonebook:
        del phonebook[surname]
        write_phonebook(phonebook)


def find_entry(surname):
    phonebook = read_phonebook()
    return phonebook.get(surname, None)


def main():
    while True:
        choice = input("�������� �������� (add/update/delete/find/quit): ").lower()
        if choice == "quit":
            break
        elif choice == "add":
            surname = input("������� �������: ")
            name = input("������� ���: ")
            phone = input("������� ����� ��������: ")
            add_entry(surname, name, phone)
        elif choice == "update":
            surname = input("������� �������: ")
            name = input("������� ����� ��� (�������� ������, ����� �� ������): ")
            phone = input("������� ����� ����� �������� (�������� ������, ����� �� ������): ")
            update_entry(surname, name, phone)
        elif choice == "delete":
            surname = input("������� ������� ��� ��������: ")
            delete_entry(surname)
        elif choice == "find":
            surname = input("������� ������� ��� ������: ")
            entry = find_entry(surname)
            if entry:
                print(f"���: {entry[0]}, ����� ��������: {entry[1]}")
            else:
                print("������ �� �������.")
        else:
            print("����������� ��������.")


if __name__ == "__main__":
    main()
