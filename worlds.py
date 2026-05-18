import random

class World:
    def __init__(self, size, goal_x, goal_y, difficulty=2):
        self.size = size
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.difficulty = difficulty
        self.rocks = []
        self.solar_stations = []
        self.craters = []
        self.generate_world()

    def generate_world(self):
        if self.difficulty == 1:
            rc, sc, cc = 3, 10, 2
        elif self.difficulty == 3:
            rc, sc, cc = 20, 2, 12
        else:
            rc, sc, cc = 8, 5, 5

        for _ in range(rc):
            self.rocks.append((random.randint(-self.size, self.size), random.randint(-self.size, self.size)))
        for _ in range(sc):
            self.solar_stations.append((random.randint(-self.size, self.size), random.randint(-self.size, self.size)))
        for _ in range(cc):
            self.craters.append((random.randint(-self.size, self.size), random.randint(-self.size, self.size)))

    def is_inside_world(self, x, y):
        return -self.size <= x <= self.size and -self.size <= y <= self.size

    def reached_goal(self, x, y):
        return x == self.goal_x and y == self.goal_y

    def check_world_elements(self, pojazd):
        pos = (pojazd.x, pojazd.y)
        
        if self.difficulty == 1:
            r_dmg, s_gain, c_dmg = 5, 40, 5
        elif self.difficulty == 3:
            r_dmg, s_gain, c_dmg = 30, 10, 25
        else:
            r_dmg, s_gain, c_dmg = 15, 20, 15

        if pos in self.rocks:
            print(f"\n[!] Wjechano w skaly. Energia -{r_dmg}")
            pojazd.remove_energy(r_dmg)
            pojazd.add_score(-5)
            pojazd.log_event("Skaly")
            self.rocks.remove(pos)

        if pos in self.solar_stations:
            print(f"\n[+] Stacja solarna! Energia +{s_gain}")
            pojazd.add_energy(s_gain)
            pojazd.add_score(15)
            pojazd.log_event("Ladowanie")
            self.solar_stations.remove(pos)

        if pos in self.craters:
            print("\n[!] KRATER. Zsuwasz sie w dol. Cofanie...")
            pojazd.x -= 5
            pojazd.y -= 5
            pojazd.path.append((pojazd.x, pojazd.y))
            pojazd.remove_energy(c_dmg)
            pojazd.add_score(-10)
            pojazd.log_event("Wpadniecie do krateru")
            self.craters.remove(pos)

    def show_world_info(self):
        print("\n--- INFO O MAPIE ---")
        print(f"Trudnosc (1-3): {self.difficulty}")
        print(f"Rozmiar: -{self.size} do {self.size}")
        print(f"Cel: ({self.goal_x}, {self.goal_y})")
        print(f"Przeszkody: {len(self.rocks)} skal, {len(self.craters)} kraterow")
        print(f"Stacje: {len(self.solar_stations)}")
