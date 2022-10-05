#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Sept 2022
# This program shows how local and global variables work
# global variable
variable_X = 25


def local_variable():
    # this shows what happens with local variables

    variable_X = 10
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print(
        "Local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".format(
            variable_X, variable_Y, variable_Z
        )
    )


def global_variable():
    # this shows what happens with global variables

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print(
        "Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".format(
            variable_X, variable_Y, variable_Z
        )
    )


def main():
    # this function shows how local and global variables work

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
