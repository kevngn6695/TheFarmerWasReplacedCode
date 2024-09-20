def restore_amount(max_carrot_seeds, max_pumpkin_seeds, max_sunflower_seeds, max_fertilizers, max_cactus_seeds, max_eggs):
	carrot_seeds = Items.Carrot_Seed
	pumpkin_seeds = Items.Pumpkin_Seed
	sunflower_seeds = Items.Sunflower_Seed
	cactus_seeds = Items.Cactus_Seed
	eggs = Items.Egg
	fertilizers = Items.Fertilizer

	trade(carrot_seeds, max_carrot_seeds)
	trade(pumpkin_seeds, max_pumpkin_seeds)
	trade(sunflower_seeds, max_sunflower_seeds)
	trade(fertilizers, max_fertilizers)
	trade(cactus_seeds, max_cactus_seeds)
	trade(eggs, max_eggs)
