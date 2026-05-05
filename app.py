if st.button("Run Strategy"):

    stay = simulate_stay_out(tire_age)
    pit = simulate_pit(pit_loss)

    if pit < stay:
        decision = "PIT"
        reason = "New tires will be faster"
    else:
        decision = "STAY OUT"
        reason = "Current tires are still good"

    st.success(f"Decision: {decision}")
    st.info(f"Reason: {reason}")