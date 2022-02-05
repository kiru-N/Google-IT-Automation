def format_address(address_string):
    # Declare variables
    house_number = 0
    street_name = ""
    # Separate the address string into parts
    address = address_string.split(' ', 1)
    # Traverse through the address parts
    for address_parts in address:

        if address_parts.isnumeric():
            house_number = address_parts
        else:
            street_name = address_parts
    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
