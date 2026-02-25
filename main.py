import os

def main():
    command = None
    try:
        aura = load_aura()
    except FileNotFoundError:
        save_aura(0)
        aura = load_aura()
    price = 3

    while True:
        os.system("clear")
        print(":'=\nhustle (? for help)")
        command = input("* ")
        if command == "$":
            input(f"{print_aura(aura)}\n")
        elif command == "0":
            # 0: waste
            if aura >= price:
                print(f"{print_aura(aura)}")
                aura -= price
                save_aura(aura)
                input(f"{print_aura(aura)}\n:)\n")
            else:
                input(f"{print_aura(aura)}\n:(\n")
        elif command == "1":
            # 1: useful
            if aura > 5:
                input(f"{print_aura(aura)}\nrelax tryhard\n")
            else:
                print(f"{print_aura(aura)}")
                aura += 1
                save_aura(aura)
                input(f"{print_aura(aura)}\n")
        elif command == "?":
            input(f"track tasks to earn leisure. {price} useful = 1 reward.\n1: useful (+1 aura)\n0: leisure (-{price} aura)\n$: aura points\n?: help\nq: quit\n")
        elif command == "q":
            os.system("clear")
            break
        else:
            continue

def print_aura(aura):
    bar = []
    for i in range(0, 6):
        if aura > 0:
            bar.append("1")
            aura -= 1
        else:
            bar.append(" ")
    return(bar)

def save_aura(var):                      
    with open('aura.txt', 'w') as file:
        file.write(str(var))

def load_aura():
    with open('aura.txt', 'r') as file:
        loaded_str = file.read()
        return int(loaded_str)


main()
