import random

def sandstorm_event(pojazd):
    print("\n[LOSOWE] Burza piaskowa! Wiatr sypie piachem.")
    pojazd.remove_energy(12)
    pojazd.add_score(-5)
    pojazd.log_event("Burza piaskowa")

def signal_event(pojazd):
    print("\n[LOSOWE] Zlapano czysty sygnal z Ziemi. Update softu.")
    pojazd.add_energy(15)
    pojazd.add_score(5)
    pojazd.log_event("Sygnal z bazy")

def mineral_event(pojazd):
    print("\n[LOSOWE] Sensory wykryly zyle rzadkich mineralow.")
    pojazd.add_score(25)
    pojazd.log_event("Ciekawa probka")

def system_failure_event(pojazd):
    print("\n[LOSOWE] Glitch w systemie jezdnym. Restart zabiera prad.")
    pojazd.remove_energy(18)
    pojazd.add_score(-10)
    pojazd.log_event("Awaria systemu")

def trigger_random_event(pojazd):
    if random.randint(1, 100) <= 30:
        ev = random.choice([sandstorm_event, signal_event, mineral_event, system_failure_event])
        ev(pojazd)
