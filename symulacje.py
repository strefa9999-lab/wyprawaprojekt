import math
from events import trigger_random_event
from turtle_view import draw_mission

def calculate_movement(angle, distance=5):
    rad = math.radians(angle)
    return round(math.cos(rad) * distance), round(math.sin(rad) * distance)

def show_controls():
    print("\nSTEROWANIE:")
    print("w - przod | a - lewo | d - prawo | q - wyjscie")

def execute_move(pojazd):
    dx, dy = calculate_movement(pojazd.angle)
    pojazd.move(dx, dy)

def handle_player_action(pojazd):
    while True:
        akcja = input("Akcja (w/a/d/q): ").lower()
        if akcja == "w":
            execute_move(pojazd)
            return True
        elif akcja == "a":
            pojazd.rotate_left()
            return True
        elif akcja == "d":
            pojazd.rotate_right()
            return True
        elif akcja == "q":
            pojazd.set_failure("Przerwane przez gracza")
            return False
        else:
            print("Zly klawisz.")

def check_end_conditions(pojazd, world, config):
    pojazd.check_energy()
    if not pojazd.alive:
        return True
    
    if not world.is_inside_world(pojazd.x, pojazd.y):
        pojazd.set_failure("Wyjazd poza mape")
        return True
        
    if world.reached_goal(pojazd.x, pojazd.y):
        pojazd.set_success()
        pojazd.add_score(100)
        return True
        
    if pojazd.steps >= config["max_steps"]:
        pojazd.set_failure("Koniec czasu (limit krokow)")
        return True
        
    return False

def run_simulation(pojazd, world, config):
    world.show_world_info()
    show_controls()
    
    while True:
        print(f"\n--- KROK {pojazd.steps + 1} ---")
        pojazd.show_status()
        
        if not handle_player_action(pojazd):
            break
            
        world.check_world_elements(pojazd)
        trigger_random_event(pojazd)
        
        if check_end_conditions(pojazd, world, config):
            break
            
    print("\nKoniec jazdy.")
    pojazd.generate_report()
    draw_mission(pojazd, world)
