def tire_degradation(tire_age):
    return 0.05 * tire_age  # simple model

def simulate_stay_out(tire_age, laps=5):
    total_time = 0
    for i in range(laps):
        lap_time = 90 + tire_degradation(tire_age + i)
        total_time += lap_time
    return total_time

def simulate_pit(pit_loss, laps=5):
    total_time = pit_loss
    for i in range(laps):
        lap_time = 90  # fresh tires
        total_time += lap_time
    return total_time

# INPUTS
tire_age = 18
pit_loss = 20

stay_time = simulate_stay_out(tire_age)
pit_time = simulate_pit(pit_loss)

if pit_time < stay_time:
    print("👉 Decision: PIT")
else:
    print("👉 Decision: STAY OUT")

print("Stay time:", stay_time)
print("Pit time:", pit_time)