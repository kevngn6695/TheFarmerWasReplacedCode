def manage_carrot(num_carrot):
	if get_entity_type() != num_carrot:
		plant(num_carrot)
	elif can_harvest():
		harvest()