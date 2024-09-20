def manage_cactus(num_cactus, total):
    n = get_world_size()
    cacti = []

    # Planting cacti
    for pos in range(n * n):
        x = pos // n
        y = pos % n
        move_to_target(x, y)
        
        if get_entity_type() != num_cactus:
            plant(num_cactus)
        cactus_size = measure()
        cacti.append((x, y, cactus_size))
    
    # Sorting cacti for harvesting
    sorted = False
    while not sorted:
        sorted = True
        for pos in range(n * n):
            x = pos // n
            y = pos % n
            move_to_target(x, y)
            cactus_size = measure()
            
            if x < n - 1 and measure(East) < cactus_size:
                swap(East)
                sorted = False
            if y < n - 1 and measure(North) < cactus_size:
                swap(North)
                sorted = False
            if x > 0 and measure(West) > cactus_size:
                swap(West)
                sorted = False
            if y > 0 and measure(South) > cactus_size:
                swap(South)
                sorted = False

    # Harvest all cacti once sorted
    for pos in range(n * n):
        x = pos // n
        y = pos % n
        move_to_target(x, y)
        if can_harvest():
            harvest()