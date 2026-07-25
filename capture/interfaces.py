from scapy.all import get_if_list


def get_interfaces():
    return get_if_list()


if __name__ == "__main__":
    print("Available Interfaces:\n")

    for index, interface in enumerate(get_interfaces(), start=1):
        print(f"{index}. {interface}")