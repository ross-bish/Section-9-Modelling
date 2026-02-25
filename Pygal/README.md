# Computational Modelling using Python & Pygal

## Lesson 1 - Human Population 👨‍👩‍👧‍👦
Human Population Growth covers exponential growth, reading and tracing the code, predicting outputs before running, and the counterintuitive result about starting population vs. growth rate.

<img width="1208" height="855" alt="image" src="https://github.com/user-attachments/assets/4c134008-ca13-4170-b074-37f389b998ae" />


## Lesson 2 - Fish Population🐟
Fish Population & Harvesting covers logistic growth vs. exponential, manually interpreting the formula, a data-collection table for the three scenarios, and finding the "tipping point" harvest rate where the population collapses.

<img width="1191" height="855" alt="image" src="https://github.com/user-attachments/assets/be2e74d1-7c4f-4ec2-ac4a-b7065280e818" />


## Lesson 3 - Forestry Conservation🌳🔥
Forestry Conservation covers 

- Part A (Fire risk) including a manual calculation exercise so students understand where the score comes from.
- Part B (Logging) comparing conservation scenarios with a data table.

<img width="1680" height="599" alt="image" src="https://github.com/user-attachments/assets/7987f6d9-b4fd-4bf3-a9da-e4c69c068c5e" />


### How this builds on the previous two lessons
The progression across all three models is intentional...
- The human population model introduced the simplest possible loop — one variable, one formula.
- The fish model added complexity with carrying capacity, harvesting, and the Euler method.
- Then the forestry model introduces multi-variable functions for the first time, where four inputs combine to produce a single output, which is a significant and transferable concept.
    - It also introduces the idea of a ``conservation_factor`` as a parameter students can tune - which naturally frames the model as a decision-making tool, not just a simulation.

A strong discussion question to close the lesson: 

**"Our models assume conditions change smoothly and predictably - but do real forests work that way? What events might cause sudden, dramatic changes that our model can't capture?"**

## 💡Chart recommendations:
For fire risk prediction, a ``pygal.Line()`` chart works best. 

Fire risk changes continuously over time as temperature, wind, and moisture shift - a line chart communicates that ongoing change naturally and lets students see tipping points where risk spikes.

For illegal logging, a ``pygal.Bar()`` chart is the better fit. 

Logging impact is more naturally thought of in discrete chunks - monthly or yearly losses of forest cover - rather than a smooth curve. A bar chart makes it easy to compare periods side by side and see cumulative damage clearly.

