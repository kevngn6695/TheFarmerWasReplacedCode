def manage_pumpkin(num_pumpkin, total):
	giant_pumpkin = True
	if get_entity_type() != num_pumpkin:
		plant(num_pumpkin)
	else:
		# Check for the formation of a giant pumpkin
		for i in range(total):
			for j in range(total):
				move_to_target(i, j)
				if get_entity_type() != num_pumpkin:
					harvest()
					giant_pumpkin = False
					if get_entity_type() == None:
						plant(num_pumpkin)
			# Harvest the giant pumpkin if it's fully grown
		if giant_pumpkin:
			move_to_target(total - 1, total - 1)
			harvest()
			return True  # Indicate that tilling should occur