class Pojazd:
    def __init__(self, mission_name, rover_name, x, y, angle, energy):
        self.mission_name = mission_name
        self.rover_name = rover_name
        self.x = x
        self.y = y
        self.angle = angle
        self.energy = energy
        self.steps = 0
        self.score = 0
        self.alive = True
        self.mission_success = False
        self.end_reason = ""
        self.path = [(x, y)]
        self.event_log = []

    def move(self, dx, dy, energy_cost=5):
        old_x = self.x
        old_y = self.y
        self.x += dx
        self.y += dy
        self.energy -= energy_cost
        self.steps += 1
        self.path.append((self.x, self.y))
        print(f"Pozycja: ({old_x}, {old_y}) -> ({self.x}, {self.y})")
        print(f"Energia po ruchu: {self.energy}")

    def rotate_left(self):
        old_angle = self.angle
        self.angle = (self.angle + 90) % 360
        print(f"Obrót lewo: {old_angle} -> {self.angle}")

    def rotate_right(self):
        old_angle = self.angle
        self.angle = (self.angle - 90) % 360
        print(f"Obrót prawo: {old_angle} -> {self.angle}")

    def add_energy(self, amount):
        self.energy += amount
        print(f"Dodano energie: +{amount}. Aktualna: {self.energy}")

    def remove_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0
        print(f"Utrata energii: -{amount}. Aktualna: {self.energy}")

    def add_score(self, points):
        self.score += points

    def log_event(self, event_text):
        self.event_log.append(event_text)

    def check_energy(self):
        if self.energy <= 0:
            self.energy = 0
            self.alive = False
            self.end_reason = "Brak energii (bateria wyczerpana)"

    def set_success(self):
        self.mission_success = True
        self.end_reason = "Dotarto do celu"

    def set_failure(self, reason):
        self.alive = False
        self.end_reason = reason

    def show_status(self):
        print("\n--- STATUS POJAZDU ---")
        print(f"Nazwa: {self.rover_name}")
        print(f"Pozycja: ({self.x}, {self.y}) Kat: {self.angle}")
        print(f"Energia: {self.energy} Krok: {self.steps}")
        print(f"Wynik: {self.score}")
        print("-" * 22)

    def generate_report(self):
        print("\n==================================")
        print("          RAPORT KONCOWY")
        print("==================================")
        print(f"Misja: {self.mission_name}")
        print(f"Pojazd: {self.rover_name}")
        print(f"Pozycja koncowa: ({self.x}, {self.y})")
        print(f"Kroki: {self.steps} | Energia: {self.energy} | Punkty: {self.score}")
        print(f"Powod: {self.end_reason}")
        print("\nZdarzenia na trasie:")
        if not self.event_log:
            print(" - nic ciekawego sie nie wydarzylo")
        else:
            for e in self.event_log:
                print(f" - {e}")
        
        print("\nSTATUS:")
        if self.mission_success:
            print(">>> SUKCES <<<")
        else:
            print(">>> PORAZKA <<<")
        print("==================================")
