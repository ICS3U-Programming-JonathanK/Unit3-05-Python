#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May 12 2021
# The program will ask the user to enter a number
# for a month (between 1 and 12). It then displays
# the month as a string to the user

def find_month(month):
    months = {
        1: "{} represents January.". format(month),
        2: "{} represents February.". format(month),
        3: "{} represents March. ". format(month),
        4: "{} represents April. ". format(month),
        5: "{} represents May. ". format(month),
        6: "{} represents June. ". format(month),
        7: "{} represents July. ". format(month),
        8: "{} represents August. ". format(month),
        9: "{} represents September. ". format(month),
        10: "{} represents October. ". format(month),
        11: "{} represents November. ". format(month),
        12: "{} represents December. ". format(month),
    }
    return months.get(month, "Error. {} does not represent a month. ".
                      format(month))


if __name__ == "__main__":
    user_month = int(input("Enter the number for a month (i.e 2 for "
                           "February): "))
    print("")
    print(find_month(user_month))
