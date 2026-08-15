# ACLE 2026 — Jeddah Reality Model
# Idea & analysis: Wansaidon

import pandas as pd
import matplotlib.pyplot as plt

# Real ACLE knockout setup used in this project
matches = 11
stadiums = 2

# Create a simple dataframe
df = pd.DataFrame({
    'City': ['Jeddah'],
    'Matches': [matches],
    'Stadiums': [stadiums]
})

# Calculate how many matches each stadium hosted on average
df['Matches_per_Stadium'] = df['Matches'] / df['Stadiums']

# Display the result
print(df)

# Plot the result
ax = df.plot(
    x='City',
    y='Matches_per_Stadium',
    kind='bar',
    rot=0,
    legend=False,
    xlabel='',
    ylabel='Matches per Stadium'
)

ax.set_title('ACLE 2026 — Jeddah Reality')
ax.bar_label(ax.containers[0], fmt='%.2f')

# Remove extra chart borders
ax.spines[['top', 'right']].set_visible(False)

plt.show()
