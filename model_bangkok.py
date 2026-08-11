# ⚽ ACLE 2026 — Bangkok What-If Model
# Synthetic scenario for portfolio analysis
# Idea & analysis: Wansaidon

print("🇹🇭 BANGKOK WHAT-IF MODEL")
print("=" * 40)

# Change these numbers when you have your final schedule data.
matches = 12
stadiums = 3
days = 8

matches_per_stadium = matches / stadiums
matches_per_day = matches / days
busy_score = matches / (stadiums * days)

print(f"Matches: {matches}")
print(f"Stadiums: {stadiums}")
print(f"Days: {days}")

print("\n📊 RESULTS")
print(f"Matches per stadium: {matches_per_stadium:.2f}")
print(f"Matches per day: {matches_per_day:.2f}")
print(f"Busy score: {busy_score:.3f}")

print("\n💡 WHAT DOES THE SCORE MEAN?")
print("The score is only a simple comparison tool.")
print("Higher score = more matches packed into fewer stadium-days.")
print("It does NOT measure pitch damage.")

print("\n🇹🇭 This is a what-if model, not an official ACLE schedule.")