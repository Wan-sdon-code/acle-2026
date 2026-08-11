# ⚽ ACLE 2026 — Jeddah Reality Model
# Replace the example values below with verified schedule data.
# Idea & analysis: Wansaidon

print("🇸🇦 JEDDAH REALITY MODEL")
print("=" * 40)

# Change these numbers after checking the official schedule.
matches = 12
stadiums = 2
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
print("It does NOT prove that a pitch will be damaged.")

print("\n🇸🇦 Replace the example values with verified ACLE schedule data.")