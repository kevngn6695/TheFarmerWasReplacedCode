def trade_item(num_carrot_seeds, num_pumpkin_seeds, num_sunflower_seeds, num_fertilizers, num_barrels, num_cactus_seeds, num_eggs):
	items = {
		"wood": num_items(Items.Wood),
		"carrot_seed": num_items(Items.Carrot_Seed),
		"pumpkin_seed": num_items(Items.Pumpkin_Seed),
		"sunflower_seed": num_items(Items.Sunflower_Seed),
		"barrel": num_items(Items.Empty_Tank),
		"water_barrel": num_items(Items.Water_Tank),
		"fertilizer": num_items(Items.Fertilizer),
		"hay": num_items(Items.Hay),
		"pumpkin": num_items(Items.Pumpkin),
		"carrot": num_items(Items.Carrot),
		"cactus_seed": num_items(Items.Cactus_Seed),
		"bone": num_items(Items.Bones)
	}
	
	max_n_items = {
		"barrel": 100000,
		"water_barrel": 100000,
		"wood": 500000,
		"sunflower_seed": 40000,
		"pumpkin_seed": 10000,
		"carrot_seed": 20000,
		"fertilizer": 10000,
		"carrot": 500000,
		"cactus_seed": 10000,
		"bone": 10000
	}

	general_buff = 5

	if items["carrot_seed"] != 0 and items["pumpkin_seed"] != 0 and items["sunflower_seed"] != 0 and items["fertilizer"] != 0 and items["water_barrel"] != 0 and items["wood"] != 0 and items["cactus_seed"] != 0 and items["bone"] != 0:
			
		# Trading for seeds
		if items["carrot_seed"] < max_n_items["carrot_seed"]:
			trade(num_carrot_seeds, general_buff)
		elif items["pumpkin_seed"] < max_n_items["pumpkin_seed"]:
			trade(num_pumpkin_seeds, general_buff)
		elif items["sunflower_seed"] < max_n_items["sunflower_seed"]:
			trade(num_sunflower_seeds, general_buff)
		elif items["cactus_seed"] < max_n_items["cactus_seed"]:
			trade(num_cactus_seeds, general_buff)
		elif items["bone"] < max_n_items["bone"]:
			trade(num_eggs, general_buff)
		# Trading for fertilizers
		if items["fertilizer"] < max_n_items["fertilizer"]:
			trade(num_fertilizers, general_buff)
		
		# Trading for empty barrels
		if items["wood"] > max_n_items["wood"] and items["water_barrel"] < max_n_items["water_barrel"]:
			trade(num_barrels)
		
	else:
		restore_amount(max_n_items["carrot_seed"], max_n_items["pumpkin_seed"], max_n_items["sunflower_seed"], max_n_items["fertilizer"], max_n_items["cactus_seed"], max_n_items["bone"])
