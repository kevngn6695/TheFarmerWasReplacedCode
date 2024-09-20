def manage_sunflower(sunflower_petals, num_sunflower):
	if get_entity_type() != num_sunflower:
		plant(num_sunflower)
		petals = measure()
	
		if petals and 7 < petals <= 15:
			sunflower_petals.append(petals)
	elif can_harvest():
		if sunflower_petals:
			max_petals = max(sunflower_petals)
			if measure() == max_petals:
				harvest()
				sunflower_petals.remove(max_petals)
