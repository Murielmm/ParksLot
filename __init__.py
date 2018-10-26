# -*- coding: utf-8 -*-
import Park
import Menu

Park = Park.park()
Menu = Menu.menu()

option = Menu.displayMainMenu()

while option != 0:

    if option == 1:
        vehicle = Menu.displayEntryMenu()

        if vehicle:
            Park.checkIn(vehicle)

    elif option == 2:
        plate = Menu.displayExitMenu()

        if plate:
            Park.checkOut(plate)

    elif option == 3:
        Park.listAllSpaces()

    option = Menu.displayMainMenu()
