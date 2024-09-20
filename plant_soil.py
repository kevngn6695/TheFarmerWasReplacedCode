def plant_soil(sunflower_petals, num_carrot, num_pumpkin, num_sunflower, water_barrel, num_cactus, num_dinosaurs, total):
    water_lvl = get_water()
    
    n_items = {
    	"sunflower_seed": num_items(Items.Sunflower_Seed),
    	"power": num_items(Items.Power),
    	"pumpkin": num_items(Items.Pumpkin),
    	"carrot": num_items(Items.Carrot),
    	"cactus": num_items(Items.Cactus),
    	"dinosaur": num_items(Items.Egg)
    }
    
    max_n_items = {
    	"sunflower_seed": 400000,
    	"power": 1000000,
    	"carrot": 5000000,
    	"pumpkin": 1000000,
    	"cactus": 10000,
    	"dinosaur": 100000
    }
    
    if water_lvl < 0.75:
        use_item(water_barrel)

	receiving_rate = 0.95
	
    # Manage sunflowers with the most petals
	#if n_items["power"] <= max_n_items["power"]:
	#	manage_sunflower(sunflower_petals, num_sunflower)
	#else:
		# If power is at max, harvest sunflower with the minimum petals
	#	if sunflower_petals:
	#		min_petals = min(sunflower_petals)
	#		if measure() == min_petals:
	#			harvest()
				

    # Manage carrots planting and harvesting in a regular way
	#if n_items["carrot"] <= (max_n_items["carrot"] * receiving_rate):
	#	manage_carrot(num_carrot)
	
	# Manage Dinosaur
	manage_dinosaurs()
			
	# Manage cactus
	#manage_cactus(num_cactus, total)
			
    # Manage pumpkin planting and harvesting a giant pumpkin formation
	#if n_items["pumpkin"] <= max_n_items["pumpkin"]:
	#	manage_pumpkin(num_pumpkin, total)
    return False  # No need to till
    