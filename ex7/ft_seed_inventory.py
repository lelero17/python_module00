def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	seed_capitalized = seed_type.capitalize()

	if unit == "packets":
		print(seed_capitalized, "seeds:", quantity, "packets available")
	elif unit == "grams":
		print(seed_capitalized, "seeds:", quantity, "grams total")
	elif unit == "area":
		print(seed_capitalized, "seeds: covers", quantity, "square meteres")
	else:
		print("Unknown unit type")
