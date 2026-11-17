# STRAT-AI — Race Strategy Simulator

STRAT-AI is a small Streamlit prototype that compares two simplified race strategies over a configurable five-lap horizon: staying out on the current tyres or making a pit stop.

The current implementation is a deterministic simulation, not a trained AI model or a live motorsport strategy system.

## What works today

- Adjust tyre age with a Streamlit slider.
- Adjust estimated pit-lane time loss.
- Estimate the total time for staying out using a simple linear tyre-degradation assumption.
- Estimate the total time after pitting using a fixed fresh-tyre lap-time assumption.
- Compare both estimates and display a **PIT** or **STAY OUT** recommendation with a short explanation.

## How the model works

The current prototype uses the following simplified assumptions:

- Base lap time: 90 seconds.
- Tyre degradation: 0.05 seconds per lap for each unit of tyre age.
- Stay-out strategy: five laps with tyre age increasing by one each lap.
- Pit strategy: pit loss plus five laps at the base lap time.

These assumptions are illustrative. They are not calibrated against real tyre, circuit, weather, fuel, traffic, or telemetry data.

## Technology

- Python
- Streamlit

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Chammx/strat-ai.git
   cd strat-ai
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, activate with `.venv\\Scripts\\activate`.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Project structure

```text
.
├── app.py            # Streamlit interface and strategy comparison
├── strategy.py       # Standalone example of the simplified calculations
└── requirements.txt # Python dependency list
```

## Current limitations

- The model uses fixed illustrative assumptions.
- It compares only two strategies and a fixed five-lap horizon in the web interface.
- It does not ingest live timing, telemetry, weather, track position, safety-car, or competitor data.
- It does not currently use an LLM, machine-learning model, or confidence-scoring system.
- The standalone `strategy.py` script uses fixed example inputs; the interactive sliders are in `app.py`.

## Live prototype

[Open the Streamlit app](https://strat-ai-ycmeydh4yuzszhqxsyog4p.streamlit.app/)

---

Built as an exploratory motorsport strategy simulation project.
