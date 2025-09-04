import matplotlib.pyplot as plt

# Percentages (hit rates)
rq1_rate = 2038 / (2038 + 607 + 2433) * 100   # Precise %
rq2_rate = 4802 / (4802 + 274) * 100          # Valid %
rq3_rate = 1417 / 5078 * 100                  # Improvement %

labels = ["RQ1 (Precise)", "RQ2 (Valid)", "RQ3 (Improved)"]
values = [rq1_rate, rq2_rate, rq3_rate]

# Plot
plt.figure(figsize=(7,5))
bars = plt.bar(labels, values, color=["#4CAF50", "#2196F3", "#9C27B0"])

# Add percentage labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", 
             ha="center", va="bottom", fontsize=10)

plt.ylabel("Hit Rate (%)")
plt.ylim(0, 100)
plt.title("Hit Rate Comparison Across RQ1, RQ2, and RQ3")
plt.tight_layout()
plt.savefig("rq_hit_rates.png", dpi=300)
plt.show()
