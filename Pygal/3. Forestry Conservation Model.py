# ══════════════════════════════════════════════════════════════════════════════
# FORESTRY CONSERVATION MODEL
# This program models two threats to a forest over time:
#   1. Fire risk  - based on environmental conditions
#   2. Illegal logging - based on deforestation rates
#
# Students can adjust the parameters in each scenario to explore
# "what-if" questions about conservation and environmental management.
# ══════════════════════════════════════════════════════════════════════════════


# ── FIRE RISK MODEL ───────────────────────────────────────────────────────────
# Calculates a fire risk score (0-100) based on four environmental factors.
# Higher temperatures, stronger winds, and lower moisture/humidity all
# increase the likelihood of a fire starting or spreading.
#
# Parameters:
#   temperature    - air temperature in degrees Celsius
#   soil_moisture  - how wet the soil is, as a percentage (0% = bone dry, 100% = saturated)
#   wind_speed     - wind speed in km/h (stronger wind spreads fire faster)
#   humidity       - relative air humidity as a percentage (0% = dry air, 100% = saturated)


import pygal


# Returns: a fire risk score between 0 (no risk) and 100 (extreme risk)
def calculate_fire_risk(temperature, soil_moisture, wind_speed, humidity):

    # Temperature contributes positively to fire risk.
    # We scale it so that 40°C contributes roughly 40 points out of 100.
    temp_factor = temperature * 1.0

    # Dry soil increases fire risk. We invert soil moisture so that
    # 0% moisture = 30 risk points, and 100% moisture = 0 risk points.
    moisture_factor = (100 - soil_moisture) * 0.3

    # Strong wind increases fire risk by helping flames spread.
    # We scale wind speed so 100 km/h contributes roughly 20 risk points.
    wind_factor = wind_speed * 0.2

    # Dry air increases fire risk. Like moisture, we invert humidity.
    # 0% humidity = 10 risk points, 100% humidity = 0 risk points.
    humidity_factor = (100 - humidity) * 0.1

    # Add all factors together to get a raw risk score
    raw_score = temp_factor + moisture_factor + wind_factor + humidity_factor

    # Clamp the result to the range 0-100 so it always represents a percentage
    return min(max(raw_score, 0), 100)


# ── FIRE RISK SIMULATION ──────────────────────────────────────────────────────
# Runs the fire risk model across a number of time steps, varying the
# environmental conditions slightly each step to simulate changing weather.

# NOTE: In a more advanced version, you could load real weather data here!

#
# Parameters:
#   base_temperature   - starting temperature (°C)
#   base_soil_moisture - starting soil moisture (%)
#   base_wind_speed    - starting wind speed (km/h)
#   base_humidity      - starting humidity (%)
#   steps              - how many time steps (e.g. days) to simulate
#   temp_increase      - how much temperature rises each step (models a heatwave)
#   moisture_loss      - how much soil moisture drops each step (models a dry period)
#
# Returns: a list of fire risk scores, one per time step
def simulate_fire_risk(base_temperature, base_soil_moisture, base_wind_speed,
                       base_humidity, steps, temp_increase=0.5, moisture_loss=1.0):
    risk_history = []

    for step in range(steps):
        # Gradually increase temperature and decrease soil moisture each step
        # to simulate a worsening heatwave over time
        current_temp     = base_temperature + (step * temp_increase)
        current_moisture = max(base_soil_moisture - (step * moisture_loss), 0)  # can't go below 0%

        # Wind and humidity stay constant in this simple model.
        # Extension task: could students make these vary too?
        risk = calculate_fire_risk(
            temperature   = current_temp,
            soil_moisture = current_moisture,
            wind_speed    = base_wind_speed,
            humidity      = base_humidity
        )
        risk_history.append(round(risk, 1))

    return risk_history


# ── ILLEGAL LOGGING MODEL ─────────────────────────────────────────────────────
# Models the loss of forest cover due to illegal logging over a number of periods.
# Each period, a percentage of the remaining forest is lost.
# Optionally, a conservation effort can be applied to slow the loss.
#
# Parameters:
#   initial_forest_cover  - starting forest area (e.g. in hectares)
#   logging_rate          - fraction of forest lost per period (e.g. 0.05 = 5%)
#   periods               - number of time periods to simulate (e.g. months or years)
#   conservation_factor   - reduces logging rate if conservation measures are in place
#                           (0.0 = no effect, 1.0 = logging completely stopped)
#
# Returns: a list of forest cover values, one per period
def simulate_logging(initial_forest_cover, logging_rate, periods, conservation_factor=0.0):
    cover_history = []
    current_cover = initial_forest_cover

    for period in range(periods):
        # Apply conservation factor to reduce the effective logging rate.
        # e.g. a conservation_factor of 0.4 reduces a 5% logging rate to 3%.
        effective_logging_rate = logging_rate * (1 - conservation_factor)

        # Remove the logged portion from the remaining forest
        current_cover = current_cover * (1 - effective_logging_rate)

        cover_history.append(round(current_cover, 1))

    return cover_history


# ══════════════════════════════════════════════════════════════════════════════
# SCENARIO DEFINITIONS
# Students can edit the values below to explore their own "what-if" questions.
# ══════════════════════════════════════════════════════════════════════════════

simulation_steps = 30  # number of days (fire model) or months (logging model)


# ── FIRE RISK SCENARIOS ───────────────────────────────────────────────────────
# Two contrasting scenarios: a dangerous heatwave vs. more moderate conditions.
# Students could ask: "At what point does fire risk become critical?"
fire_scenarios = [
    {
        "label":              "Heatwave Conditions",
        "base_temperature":   35,    # hot starting temperature
        "base_soil_moisture": 30,    # already fairly dry soil
        "base_wind_speed":    40,    # strong wind
        "base_humidity":      20,    # dry air
        "temp_increase":      0.8,   # temperature rises quickly each day
        "moisture_loss":      1.5,   # soil dries out quickly
    },
    {
        "label":              "Moderate Conditions",
        "base_temperature":   22,    # cooler starting temperature
        "base_soil_moisture": 60,    # reasonably moist soil
        "base_wind_speed":    15,    # light wind
        "base_humidity":      55,    # humid air
        "temp_increase":      0.3,   # temperature rises slowly
        "moisture_loss":      0.5,   # soil dries slowly
    },
]

# ── LOGGING SCENARIOS ─────────────────────────────────────────────────────────
# Two scenarios: unprotected forest vs. forest with active conservation.
# Students could ask: "How much difference does conservation actually make?"
logging_scenarios = [
    {
        "label":                "No Conservation",
        "initial_forest_cover": 10000,       # 10,000 hectares of forest
        "logging_rate":         0.05,         # 5% of remaining forest lost per month
        "conservation_factor":  0.0,          # no conservation measures in place
    },
    {
        "label":                "Active Conservation",
        "initial_forest_cover": 10000,        # same starting forest
        "logging_rate":         0.05,          # same logging pressure
        "conservation_factor":  0.6,           # conservation reduces logging by 60%
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# CHART 1: FIRE RISK — LINE CHART
# A line chart suits fire risk because risk changes continuously over time.
# Students can clearly see the point where risk accelerates and becomes critical.
# ══════════════════════════════════════════════════════════════════════════════

fire_chart = pygal.Line(
    title        = 'Forest Fire Risk Over Time: What-if Scenarios',
    x_title      = 'Day',
    y_title      = 'Fire Risk Score (0 = Safe, 100 = Extreme)',
    x_label_rotation = 45,
    show_minor_x_labels = False
)

# Label the x-axis with day numbers
fire_chart.x_labels = [f"Day {d + 1}" for d in range(simulation_steps)]

# Run each fire scenario and add it as a line on the chart
for scenario in fire_scenarios:
    risk_data = simulate_fire_risk(
        base_temperature   = scenario["base_temperature"],
        base_soil_moisture = scenario["base_soil_moisture"],
        base_wind_speed    = scenario["base_wind_speed"],
        base_humidity      = scenario["base_humidity"],
        steps              = simulation_steps,
        temp_increase      = scenario["temp_increase"],
        moisture_loss      = scenario["moisture_loss"]
    )
    fire_chart.add(scenario["label"], risk_data)

# Save the fire risk chart as an interactive SVG file
fire_chart.render_to_file('forest_fire_risk.svg')
print("Fire risk chart saved to forest_fire_risk.svg")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 2: ILLEGAL LOGGING — BAR CHART
# A bar chart suits logging because forest loss is measured in discrete periods.
# Side-by-side bars make it easy to compare protected vs. unprotected forest
# at each point in time, clearly showing the impact of conservation over months.
# ══════════════════════════════════════════════════════════════════════════════

logging_chart = pygal.Bar(
    title   = 'Forest Cover Over Time: Impact of Illegal Logging',
    x_title = 'Month',
    y_title = 'Forest Cover (hectares)',
    x_label_rotation = 45,
    show_minor_x_labels = False
)

# Label the x-axis with month numbers
logging_chart.x_labels = [f"Month {m + 1}" for m in range(simulation_steps)]

# Run each logging scenario and add it as a bar series on the chart
for scenario in logging_scenarios:
    cover_data = simulate_logging(
        initial_forest_cover = scenario["initial_forest_cover"],
        logging_rate         = scenario["logging_rate"],
        periods              = simulation_steps,
        conservation_factor  = scenario["conservation_factor"]
    )
    logging_chart.add(scenario["label"], cover_data)

# Save the logging chart as an interactive SVG file
logging_chart.render_to_file('forest_logging_impact.svg')
print("Logging impact chart saved to forest_logging_impact.svg")
