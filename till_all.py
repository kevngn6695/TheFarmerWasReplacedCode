def till_all():
    s = get_world_size()
    for position in range(s * s):
        x_pos = position // s
        y_pos = position % s
        move_to_target(x_pos, y_pos)
        if get_ground_type() == Grounds.Soil:
            till()
        elif get_ground_type() == Grounds.Turf and get_entity_type() == Entities.Grass:
			clear()