from rekins import Rekins

def main():
    print("Sveiki! Šī ir rēķinu programma")
    print("Šī programma palīdzēs ar rēķiniem un saglabās tos")

klients = input("Ievadiet klienta vārdu: ")
veltijums = input("Ievadiet veltījumu")
platums = int(input("Ievadiet platumu (mm): "))
garums = int(input("Ievadiet garumu (mm): "))
augstums = int(input("Ievadiet augstumu (mm): "))
materials = float(input("Ievadiet materāla cenu (EUR): "))

rekins = Rekins(klients, veltijums, [platums, garums, augstums], materials)
rekins.saglabat()
rekins.izdrukat_rekinu()