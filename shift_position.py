def shift_list_position(number_list: list, shift: int) -> list:
    """
    This function accepts an integer list and an integer shift value as parameters, and returns a new list with the
     elements shifted to the left by the shift value.
    :param number_list: The list of integers to shift
    :param shift: The number of positions to shift the list to the left
    :return: A new list with the elements shifted to the left by the shift value
    """
    temp_list = []

    # Verify the shift number is a positive integer and the list is populated; if it is not, exit gracefully and
    # display the error
    try:
        if not number_list:
            raise ValueError("The number list must be populated.")
        if shift < 0:
            raise ValueError("Shift value must be a positive integer.")
    except ValueError as e:
        print(e)
        return []

    """
    If the shift number is a multiple of the length of the list, that would be considered a full rotation of the
    list.  So to handle the scenario of a shift that is greater than the length of the list, we use the modulo 
    operator whose remainder will be the 'actual' shift in the list.
    """
    if shift > len(number_list):
        shift = shift % len(number_list)

    # Left shifted numbers appended to a temp list, then temp list is added to the original number list
    for i in range(0, shift):
        temp_list.append(number_list.pop(0))

    number_list.extend(temp_list)

    return number_list


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    shift = 4
    print("Input list: {}, shift: {}.".format(numbers, shift))
    print("Output: {}".format(shift_list_position(numbers, shift)))

    numbers = [1, 2, 3, 4, 5, 6, 7]
    shift = 10
    print("Input list: {}, shift: {}.".format(numbers, shift))
    print("Output: {}".format(shift_list_position(numbers, shift)))

    numbers = [1, 2, 3, 4, 5, 6, 7]
    shift = -6
    print("Input list: {}, shift: {}.".format(numbers, shift))
    print("Output: {}".format(shift_list_position(numbers, shift)))

    numbers = []
    shift = 6
    print("Input list: {}, shift: {}.".format(numbers, shift))
    print("Output: {}".format(shift_list_position(numbers, shift)))


if __name__ == "__main__":
    main()
