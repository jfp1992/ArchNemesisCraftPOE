from data import *
import os


def check_dependency(my_list, list_name):
    if checker(my_list)[0]:
        print(f'Dependencies available for {list_name}')
        return True
    else:
        print(f'Dependency {checker(my_list)[1]} is missing for {list_name}')
        return False


inv_lines = []

running = True
adding = True
crafting = False
while running:
    while True:
        while adding:
            try:
                print_count = 1
                for i in all_items:
                    if print_count % 3 != 0:
                        print(f"{(str(str(print_count) + '.').ljust(3) + i).ljust(20)}\t", end='')
                    else:
                        print(f"{(str(str(print_count) + '.').ljust(3) + i).ljust(20)}")
                    print_count += 1
                print()
                print(f'{print_count}. Go to craft checking')
                arch_choice = int(input('Please choose an arch to add to pool:'))
                os.system('cls')
            except ValueError:
                print('Choose a fucking number.')
                continue
            if not arch_choice == len(all_items) + 1:
                with open("inventory.txt", "r") as f:
                    inv_lines = f.readlines()
                if f'{all_items[arch_choice-1]}\n' not in inv_lines:
                    with open("inventory.txt", "a") as f:
                        f.write(all_items[arch_choice-1])
                        f.write('\n')
                else:
                    with open("inventory.txt", "w") as f:
                        for line in inv_lines:
                            if line.strip("\n") != all_items[arch_choice-1]:
                                f.write(line)
            else:
                adding = False
                crafting = True
                break

        while crafting:
            try:
                print_count = 1
                for i in all_craft_names:
                    if print_count % 3 != 0:
                        print(f"{(str(str(print_count) + '.').ljust(3) + i).ljust(20)}\t", end='')
                    else:
                        print(f"{(str(str(print_count) + '.').ljust(3) + i).ljust(20)}")
                    print_count += 1
                print()
                print(f'{print_count}. Go to adding / removal')
                arch_choice = int(input('Please choose a craft to test:'))
                os.system('cls')
            except ValueError:
                print('Choose a fucking number.')
                continue
            if not arch_choice == len(all_craft_names) + 1:
                check_dependency(all_crafts[arch_choice - 1], all_craft_names[arch_choice - 1])
            else:
                adding = True
                crafting = False
                break
