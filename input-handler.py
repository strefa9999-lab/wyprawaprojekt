def get_string_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("B³¹d: Pole nie mo¿e byæ puste.")

def get_int_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"B³¹d: Podaj liczbê z zakresu {min_val} do {max_val}.")
        except ValueError:
            print("B³¹d: To musi byæ liczba ca³kowita.")

def get_angle_input(prompt):
    return get_int_input(prompt, 0, 359)