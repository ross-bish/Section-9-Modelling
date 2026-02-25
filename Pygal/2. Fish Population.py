# ----------------------------------------
# Pygal Modelling - Fish population
# Date: 24/2/26
# ----------------------------------------


import pygal

# ── FISH POPULATION MODEL ──────────────────────────────────────────────────────
# This function calculates how much the fish population changes in one time step.
# It uses the logistic growth model, which is a common way to model populations
# in nature. The population grows quickly when small, slows as it approaches the
# carrying capacity, and is reduced by harvesting.
#
# Parameters:
#   population        - current number of fish
#   growthRate        - how fast the fish reproduce (higher = faster growth)
#   carryingCapacity  - the maximum population the environment can support
#   harvestRate       - how many fish are removed per unit of time (e.g. by fishing)
#
# Returns: the rate of change of the population at this moment in time
def fishModel(population, growthRate, carryingCapacity, harvestRate):
    return growthRate * population * (1 - population / carryingCapacity) - harvestRate


# ── SIMULATION PARAMETERS ─────────────────────────────────────────────────────
timeStep = 0.1   # how much time passes between each calculation (smaller = more accurate)
totalTime = 20   # how long the simulation runs (e.g. 20 years)
numSteps = int(totalTime / timeStep)  # total number of calculation steps needed


# ── WHAT-IF SCENARIOS ─────────────────────────────────────────────────────────
# Each scenario is a dictionary containing the starting conditions for one simulation run.
# By changing the initial population and harvest rate, we can compare different outcomes.
# All three scenarios use the same growth rate and carrying capacity (defined in the loop below).
scenarios = [
    {"initial_population": 50, "harvestRate": 5,  "label": "Moderate Harvest"},
    {"initial_population": 50, "harvestRate": 10, "label": "Large Harvest"},
    {"initial_population": 30, "harvestRate": 5,  "label": "Low Initial Population"},
]


# ── TIME POINTS ───────────────────────────────────────────────────────────────
# Build a list of time values for each step: [0.0, 0.1, 0.2, ..., 20.0]
# This represents the x-axis of our chart (time passing during the simulation).
time_points = [step * timeStep for step in range(numSteps + 1)]


# ── CREATE THE CHART ──────────────────────────────────────────────────────────
# pygal.Line() creates an interactive line chart object.
# We pass in axis labels and a title to make the chart easy to read.
lineChart = pygal.Line(
    x_title='Time',
    y_title='Fish Population',
    title='Fish Population: What-if Scenarios'
)


# ── RUN SIMULATIONS AND POPULATE THE CHART ────────────────────────────────────
# Loop through each scenario and simulate the fish population over time.
for scenario in scenarios:

    # Start the population history list with just the initial population value
    popHistory = [scenario["initial_population"]]

    # Simulate each time step using Euler's method:
    # next value = current value + (rate of change × time step size)
    # This is a simple but effective way to approximate how a system evolves over time.
    for step in range(1, numSteps + 1):
        currentPop = popHistory[-1]  # grab the most recently calculated population

        nextPop = currentPop + timeStep * fishModel(
            currentPop,
            growthRate=0.5,          # fish reproduce at 50% of their capacity per time unit
            carryingCapacity=100,    # the environment supports a maximum of 100 fish
            harvestRate=scenario["harvestRate"]
        )

        # Prevent the population going negative — in reality, fish can't number below zero.
        # If the model calculates a negative value, we cap it at zero (extinction).
        popHistory.append(max(nextPop, 0))

    # Add this scenario's population history as a line on the chart.
    # The label (e.g. "Moderate Harvest") will appear in the chart legend.
    lineChart.add(scenario["label"], popHistory)


# ── RENDER THE CHART ──────────────────────────────────────────────────────────
# Save the finished chart as an SVG file.
# SVG (Scalable Vector Graphics) is an interactive format that can be:
#   - opened directly in a web browser
#   - embedded into a web page
#   - scaled to any size without losing quality
lineChart.render_to_file('fish_population_what_if.svg')
