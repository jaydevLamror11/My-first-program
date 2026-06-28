results = ["Mario", "Luigi" ]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong jr."])
results.remove(["Bowser", "Donkey Kong jr."])
results.extend(["Bowser", "Donkey Kong jr"])

print(results)