def solve_maze():
    directions = [North, East, South, West]
    dir_index = 0
    
    while get_entity_type() != Entities.Treasure:
		if move(directions[dir_index]):
			if get_entity_type() == Entities.Treasure:
				harvest()
				return True
				
			dir_index = turn_left(dir_index)
		else:
			dir_index = turn_right(dir_index)
    
    return False