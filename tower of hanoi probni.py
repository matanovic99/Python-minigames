
label start:

    # slike
   # image disk1 = "disk1.png"
   # image disk2 = "disk2.png"
   # image disk3 = "disk3.png"
   # image tower = "tower.png"

    # Initializacija Tower of Hanoi
     $ tower_of_hanoi = [[3, 2, 1], [], []]

    # Funcija za prikaz trenutnog stanja tornja
    python:
        def display_towers():
            for i in range(3):
                renpy.show(tower, xpos=i * 300 + 50, ypos=100)
                for j, disk in enumerate(tower_of_hanoi[i]):
                    renpy.show(get_disk_image(disk), xpos=i * 300 + 50, ypos=300 - j * 100)

        def get_disk_image(disk):
            if disk == 1:
                return "disk1"
            elif disk == 2:
                return "disk2"
            elif disk == 3:
                return "disk3"
            else:
                return None

    # Funcija za premjestanje
    python:
        def hanoi_move(source, target):
            disk = tower_of_hanoi[source].pop()
            tower_of_hanoi[target].append(disk)

    # game loop
    while True:
        python:

            display_towers()

        menu:
            "Select a move:"
            "1. Move from Tower 1 to Tower 2"
            "2. Move from Tower 1 to Tower 3"
            "3. Move from Tower 2 to Tower 1"
            "4. Move from Tower 2 to Tower 3"
            "5. Move from Tower 3 to Tower 1"
            "6. Move from Tower 3 to Tower 2"
            "7. Quit"

        if _selected == 7:
            "Thanks for playing!"
            return
        else:
            # Obavljanje odabranog koraka
            python:
                move_mapping = {1: (0, 1), 2: (0, 2), 3: (1, 0), 4: (1, 2), 5: (2, 0), 6: (2, 1)}
                move = move_mapping[_selected]
                hanoi_move(*move)


            # provjera je li dobro rijeseno
            if tower_of_hanoi[2] == [3, 2, 1]:
                "Congratulations! You solved the Tower of Hanoi!"
                return
