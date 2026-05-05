import streamlit as st

st.title("🏁 STRAT-AI")

st.write("Welcome to your Race Strategy AI 🚀")

def tire_degradation(tire_age):
    return 0.05 * tire_age

def simulate_stay_out(tire_age):
    total = 0
    for i in range(5):
        total += 90 + tire_degradation(tire_age + i)
    return total

def simulate_pit(pit_loss):
    total = pit_loss
    for i in range(5):
        total += 90
    return total

tire_age = st.slider("Tire Age", 0, 30, 15)
pit_loss = st.slider("Pit Loss", 15, 30, 20)

if st.button("Run Strategy"):
    stay = simulate_stay_out(tire_age)
    pit = simulate_pit(pit_loss)

    if pit < stay:
        decision = "PIT"
    else:
        decision = "STAY OUT"

    st.success(f"Decision: {decision}")