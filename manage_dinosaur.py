def manage_dinosaurs():
    n = get_world_size() # Assuming the grid is 10x10
    
    # Step 1: Move across the entire grid and spawn dinosaurs
    for x in range(n):
        for y in range(n):
            move_to_target(x, y)
            if num_items(Items.Egg) > 0:
                use_item(Items.Egg)

    # Step 2: Group and harvest dinosaurs
    visited = set()
    dinosaur_groups = []

    for x in range(n):
        for y in range(n):
            move_to_target(x, y)
            dinosaur_type = measure()
            
            if dinosaur_type != 0:  # Assuming 0 means no dinosaur present
                if (x, y) not in visited:
                    group = find_connected_group(x, y, dinosaur_type, n, visited)
                    if len(group) >= 4:
                        dinosaur_groups.append(group)

    # Harvest optimal groups of dinosaurs
    for group in dinosaur_groups:
        if group:  # Ensure the group is not empty
            x, y = group[0]  # Move to the first dinosaur in the group
            move_to_target(x, y)
            harvest()

def find_connected_group(x, y, dinosaur_type, n, visited):
    group = []
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        
        move_to_target(cx, cy)
        if measure() == dinosaur_type:
            group.append((cx, cy))

            # Add neighbors to stack considering farm wrapping
            stack.append(((cx + 1) % n, cy))
            stack.append(((cx - 1) % n, cy))
            stack.append((cx, (cy + 1) % n))
            stack.append((cx, (cy - 1) % n))
    
    return group
    