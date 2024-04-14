from os import system
from pyfiglet import Figlet
from icecream import ic


def main() -> None:
    title()
    input_type: str = get_type("input")
    target_type: str = get_type("target", input_type)


def title(error_message: str = "") -> None:
    """
    Clear console and display title.
    Optional: display a red error message
    """
    system("cls")
    print("\033[96m \033[1m" + generate_title())  # Cyan Bold
    print("\033[93m \n" + error_message)
    print("\033[0m")  # No color
    # Colors from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal


def get_type(get_case: str, input_type="") -> str:
    """
    Prompt the user for a data type.
    Based on get_case ("input" | "target").
    If used for "target", second argument should be input type
    Features:
        - Display menu
        - Display prompt
        - Call Repair_input
        - Error handling with title()
    """
    match get_case:
        case "input":
            title_message = "Available data types"
            input_message = "Select input data type: "
        case "target":
            title_message = f"Available conversions for {input_type}"
            input_message = "Select target data type: "

    error: str = ""
    while True:
        title(error)
        print(menu_title(title_message))
        menu: list[str] = get_menu(input_type)
        print(load_menu(menu))

        try:
            return repair_input(input(input_message).strip().lower(), menu)
        except ValueError:
            error = "That's not a valid type"
            continue


def generate_title(
    title: str = "Converter", description: str = "Edit data easily!"
) -> str:
    title_renderer = Figlet(font="cosmic", width=300)
    description_renderer = Figlet(font="big", width=300)

    description = description.replace(" ", "  ")
    return f"{title_renderer.renderText(title)}\n{description_renderer.renderText(description)}"


def repair_input(input: str, data_types: list[str]) -> str:
    ic(data_types)
    if input in data_types and input == "ascii":
        return "ASCII"
    elif input.title() in data_types:
        return input.title()
    else:
        try:
            int(input)
            return data_types[input - 1]
        except:
            raise ValueError()


def get_menu(selected_data_type: str = "") -> list[str]:
    """Returns the menu based on the selected data type, default is all items"""

    data_types: list[str] = ["Text", "Number", "Binary", "Hex", "Morse", "ASCII"]
    data_type_compatibility: dict[str, list[str]] = {
        "": data_types,
        "Text": data_types[2:],
        "Number": data_types[2:],
        "Binary": [type for type in data_types if type != "Binary"],
        "Hex": [type for type in data_types if type != "Hex"],
        "Morse": [type for type in data_types if type != "Morse"],
        "ASCII": [type for type in data_types if type != "ASCII"],
    }

    return data_type_compatibility[selected_data_type]


def menu_title(menu_title: str) -> str:
    left_spacing, right_spacing = calculate_spacing(menu_title, 20)
    return f" \n||{left_spacing}{menu_title}{right_spacing}||"


def load_menu(menu_list: list[str]) -> str:
    menu: list[str] = []
    for i, menu_item in enumerate(menu_list):
        left_spacing, right_spacing = calculate_spacing(menu_item, 10)
        menu.append(f"|[{i + 1}]|  |{left_spacing}{menu_item}{right_spacing}|")
    return f"{'\n'.join(menu)}\n"


def calculate_spacing(item: str, menu_length: int) -> str:
    item_length: int = len(item)
    # ↓ Make an even item_length for calculating spacing_amount division
    even_item_length: int = item_length
    if item_length % 2 != 0:
        even_item_length += 1

    spacing_amount: int = int((menu_length - even_item_length) / 2)

    left_spacing: str = " " * spacing_amount
    right_spacing: str = " " * (menu_length - spacing_amount - item_length)

    return left_spacing, right_spacing


if __name__ == "__main__":
    main()
