# ACLE 2026 — Bangkok What-If vs Jeddah Reality
# Idea & analysis: Wansaidon

import pandas as pd
import matplotlib.pyplot as plt

# Create the comparison data
data = {
    'City': ['Bangkok', 'Jeddah'],
    'Type': ['What-If', 'Reality'],
    'Matches': [11, 11],
    'Stadiums': [3, 2]
}

df = pd.DataFrame(data)

# Calculate average matches per stadium
df['Matches_per_Stadium'] = df['Matches'] / df['Stadiums']

# Display the dataframe
print(df)

# Sort from lower to higher stadium load
df = df.sort_values(by='Matches_per_Stadium')

# Plot the comparison
ax = df.plot(
    x='City',
    y='Matches_per_Stadium',
    kind='bar',
    rot=0,
    legend=False,
    xlabel='',
    ylabel='Matches per Stadium'
)

ax.set_title('ACLE 2026 — Stadium Load Comparison', y=1.05)
ax.bar_label(ax.containers[0], fmt='%.2f')

# Remove extra chart borders
ax.spines[['top', 'right']].set_visible(False)

plt.show()
