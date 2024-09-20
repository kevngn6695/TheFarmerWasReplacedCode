def move_to_target(x_pos, y_pos):
	# Move to the target direciton
	while get_pos_x() != x_pos: # Loop if x-position is not the current position
		if x_pos > get_pos_x():
			move(East)
		else:
			move(West)
			
	while get_pos_y() != y_pos: # Loop if y-position is not the current position
		if y_pos > get_pos_y():
			move(North)
		else:
			move(South)

	return get_pos_x(), get_pos_y()
	