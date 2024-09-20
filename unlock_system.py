def unlock_system(unlock_items):
	# Auto Unlocks
	for unlock_item in unlock_items:
		if get_cost(unlock_item):
			unlock(unlock_item)