#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program converts celsius to fahrenheit using functions


def fahrenheit():
    # This function converts celsius to fahrenheit using functions

    tc_as_string = input("Enter a temperature(°C): ")
    try:
        tc = float(tc_as_string)
        tf = (9 / 5) * tc + 32

        print("\n{0}°C is equal to {1}°F.".format(tc, tf))

    except:
        print("\nInvalid Input")


def main():
    # this function runs the fahrenheit function

    fahrenheit()

    print("\nDone.")


if __name__ == "__main__":
    main()
