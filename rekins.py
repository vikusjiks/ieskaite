from datetime import datetime

class Rekins:
    def __init__(self, klients, veltijums, izmers, materials):
        self.klienta_vards = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials
        self.laiks = datetime.now().strftime("%d_%m_%Y_%H:%M:%S")
        self.rekina_summa = self.aprekins()

    def aprekins(self):
        platums, garums, augstums = self.izmers
        darba_samaksa = 15
        PVN = 21
        produkta_cena = (len(self.veltijums) * 1.2) + ((platums / 100) * (garums / 100) * (augstums / 100) / 3) * self.materials
        PVN_summa = (produkta_cena + darba_samaksa) * PVN / 100
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
        return rekina_summa

    def izdrukat_rekinu(self):
        print(f"Rēķina izveidošanas laiks: {self.laiks}")
        print(f"Klienta vārds: {self.klienta_vards}")
        print(f"Veltījums: {self.veltijums}")
        print(f"Lādītes izmēri (platums x garums x augstums): {self.izmers[0]} x {self.izmers[1]} x {self.izmers[2]} mm")
        print(f"Materiāla cena EUR/m^2): {self.materials}")
        print(f"Rēķina summa: {self.rekina_summa:.2f} EUR")

    def saglabat(self):
        faila_nosaukums = f"{self.klienta_vards}_{self.laiks}.txt"
        with open(faila_nosaukums, 'w') as f:
            f.write(f"Rēķina izveidošanas laiks: {self.laiks}\n")
            f.write(f"Klienta vārds: {self.klienta_vards}\n")
            f.write(f"Veltījums: {self.veltijums}\n")
            f.write(f"Lādītes izmēri (platums x garums x augstums): {self.izmers[0]} x {self.izmers[1]} x {self.izmers[2]} mm")
            f.write(f"Materiāla cena EUR/m^2: {self.materials}\n")
            f.write(f"Rēķina summa: {self.rekina_summa:.2f} EUR\n")
            print(f"Rēķins saglabāts kā {faila_nosaukums}\n")