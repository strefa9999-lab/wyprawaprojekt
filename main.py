import json
from rover import Pojazd
from world import World
from simulation import run_simulation
from input_handler import get_string_input, get_int_input, get_angle_input

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def create_pojazd():
    print("\n-- KREATOR POJAZDU --")
    m_name = get_string_input("Misja (nazwa): ")
    p_name = get_string_input("Pojazd (nazwa): ")
    x = get_int_input("Start X (-100 do 100): ", -100, 100)
    y = get_int_input("Start Y (-100 do 100): ", -100, 100)
    ang = get_angle_input("Kat (0-359): ")
    en = get_int_input("Energia (1-500): ", 1, 500)
    
    return Pojazd(m_name, p_name, x, y, ang, en)

def main():
    config = load_config()
    
    while True:
        print("\n" + "="*30)
        print("    MARS ROVER GAME")
        print("="*30)
        
        print("Poziom trudnosci:")
        print("1 - Spacer (duzo energii, malo skal)")
        print("2 - Normalny")
        print("3 - Pieklo (malo czasu, duzo kraterow)")
        
        diff = get_int_input("Wybierz (1-3): ", 1, 3)
        
        if diff == 1:
            config["max_steps"] = 80
        elif diff == 3:
            config["max_steps"] = 30
        else:
            config["max_steps"] = 50
            
        world = World(config["world_size"], config["goal_x"], config["goal_y"], diff)
        pojazd = create_pojazd()
        
        input("\nWcisnij ENTER zeby zaczac...")
        run_simulation(pojazd, world, config)
        
        if input("\nJeszcze raz? (t/n): ").lower() != 't':
            break

if __name__ == "__main__":
    main()
