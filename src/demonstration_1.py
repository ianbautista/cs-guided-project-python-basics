"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""

# should return an array


def split_in_parts(string, part_length):
    # Your code here

    # regular version
    # output = []
    # for index in range(0, len(s), part_length):
    #     output.append(s[index: index + part_length])
    # return output

    # list comprehension version (fancy syntax)
    return [string[index:index + part_length] for index in range(0, len(string), part_length)]


print(split_in_parts("supercalifragilisticexpialidocious", 3))

# Your code here
