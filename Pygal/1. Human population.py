# -----------------------------------
# Pygal Modelling - Human Population
# Date: 24/2/26
# -----------------------------------

import pygal

# ── HUMAN POPULATION MODEL ────────────────────────────────────────────────────
# This function simulates exponential population growth over a number of years.
# Unlike the fish model, there is no carrying capacity or harvesting — the
# population simply grows by a fixed percentage each year (compound growth).
# This mirrors how human populations are often modelled at a basic level.
#
# Parameters:
#   population  - the starting population
#   growth_rate - the annual growth rate as a decimal (e.g. 0.05 = 5% per year)
#   years       - how many years to simulate
#
# Returns: a list of population values, one per year
def run_population_model(population, growth_rate, years):
    history = []
    for year in range(years):
        # Each year, the population increases by the growth rate percentage.
        # This is compound growth: growth builds on the previous year's total.
        population = population * (1 + growth_rate)
        history.append(round(population))  # round to whole people
    return history


# ── SIMULATION PARAMETERS ─────────────────────────────────────────────────────
starting_population = 1000  # initial population at year 0
years = 20                  # how many years to simulate


# ── WHAT-IF SCENARIOS ─────────────────────────────────────────────────────────
# Each scenario adjusts either the starting population or the growth rate.
# This lets students explore questions like:
#   "What happens if a population grows faster?"
#   "Does a larger starting population always mean more people long-term?"
scenarios = [
    {"initial_population": 1000, "growth_rate": 0.02, "label": "Low Growth (2%)"},
    {"initial_population": 1000, "growth_rate": 0.05, "label": "Moderate Growth (5%)"},
    {"initial_population": 1000, "growth_rate": 0.10, "label": "High Growth (10%)"},
    {"initial_population": 500,  "growth_rate": 0.05, "label": "Half Starting Population (5%)"},
]


# ── TIME POINTS ───────────────────────────────────────────────────────────────
# Build a list of year labels for the x-axis: ["Year 1", "Year 2", ..., "Year 20"]
year_labels = [f"Year {y + 1}" for y in range(years)]


# ── CREATE THE CHART ──────────────────────────────────────────────────────────
# pygal.Line() creates an interactive line chart.
# disable_xml_declaration makes the SVG easier to embed directly into a web page.
lineChart = pygal.Line(
    x_title='Year',
    y_title='Population',
    title='Human Population Growth: What-if Scenarios',
    x_label_rotation=45,    # rotate x-axis labels so they don't overlap
    show_minor_x_labels=False
)

# Attach the year labels to the x-axis so each point is clearly labelled
lineChart.x_labels = year_labels


# ── RUN SIMULATIONS AND POPULATE THE CHART ────────────────────────────────────
# Run the model for each scenario and add the results as a line on the chart.
for scenario in scenarios:

    # Run the population model for this scenario's starting conditions
    population_history = run_population_model(
        scenario["initial_population"],
        scenario["growth_rate"],
        years
    )

    # Add this scenario's results to the chart.
    # The label will appear in the interactive legend.
    lineChart.add(scenario["label"], population_history)


# ── RENDER THE CHART ──────────────────────────────────────────────────────────
# Save the chart as an interactive SVG file.
# Open it in a web browser to explore the data — hover over points to see values.
lineChart.render_to_file('human_population_growth.svg')


