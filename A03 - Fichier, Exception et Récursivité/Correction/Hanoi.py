def write_and_print(string, file):
    print(string)
    file.write(string + "\n")


def hanoi(n, A, B, C, file):
    if n == 1:
        write_and_print(f"Disk {n} from {A} to {B}", file)
        return
    hanoi(n - 1, A, C, B, file)
    write_and_print(f"Disk {n} from {A} to {B}", file)
    hanoi(n - 1, C, B, A, file)


# w+ va créer et écraser le fichier
with open("log.txt", "w+", encoding="utf-8") as file:
    hanoi(3, "A", "B", "C", file)
