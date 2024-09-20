def plant_turf(bush, tree, grass, fertilizer):
	n_items = {
		"hay": num_items(Items.Hay),
		"wood": num_items(Items.Wood),
		"gold": num_items(Items.Gold)
	}
	
	max_n_items = {
		"hay": 1000000,
		"wood": 3000000,
		"gold": 1000000
	}
	
	if get_entity_type() == grass and can_harvest():
		harvest()

	if get_entity_type() not in [tree, bush]:
		if (is_even(get_pos_x()) and is_even(get_pos_y())) or (is_odd(get_pos_x()) and is_odd(get_pos_y())):
			plant(tree)
			use_item(fertilizer)
		else:
			plant(bush)
			use_item(fertilizer)
			use_item(Items.Power)
	
	if get_entity_type() in [tree, bush] and can_harvest():
		harvest()
		till()

	# Check if the current entity is a hedge
	if get_entity_type() == Entities.Hedge and solve_maze():
		clear()

	return False   
	