import os

def main():
    command = None
    aura = 0
    price = 3

    while True:
        os.system("clear")
        print(":'=\nhustle")
        command = input("* ")
        if command == "$":
            input(f"{print_aura(aura)}\n")
        elif command == "0":
            # 0: waste
            if aura >= price:
                print(f"{print_aura(aura)}")
                aura -= price
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
                input(f"{print_aura(aura)}\n")
        elif command == "?":
            input("help page")
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

main()
