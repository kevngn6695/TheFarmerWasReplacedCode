clear()

def main():
    sunflower_list = []
    
    start_benchmark_time = 0
	start_benchmark_op_count = 0
    
    # Infinite Loop for running the drone
    while True:
        entities = {
        	"bush": Entities.Bush,
        	"carrot": Entities.Carrots,
        	"grass": Entities.Grass,
        	"tree": Entities.Tree,
        	"pumpkin": Entities.Pumpkin,
        	"sunflower": Entities.Sunflower,
        	"cactus": Entities.Cactus,
        	"dinosaur": Entities.Dinosaur
        }
        
        items = {
        	"carrot_seed": Items.Carrot_Seed,
        	"pumpkin_seed": Items.Pumpkin_Seed,
        	"sunflower_seed": Items.Sunflower_Seed,
        	"barrel": Items.Empty_Tank,
        	"water_barrel": Items.Water_Tank,
        	"fertilizer": Items.Fertilizer,
        	"cactus_seed": Items.Cactus_Seed,
        	"cactus": Items.Cactus,
        	"dinosaur_egg": Items.Egg
        }
        
        unlock_items = [
            Unlocks.Auto_Unlock, Unlocks.Benchmark, Unlocks.Cactus, Unlocks.Carrots, Unlocks.Costs, Unlocks.Debug, 
            Unlocks.Debug_2, Unlocks.Dictionaries, Unlocks.Expand, Unlocks.Fertilizer, Unlocks.Functions, 
            Unlocks.Grass, Unlocks.Lists, Unlocks.Loops, Unlocks.Mazes, Unlocks.Multi_Trade, Unlocks.Operators, 
            Unlocks.Plant, Unlocks.Polyculture, Unlocks.Pumpkins, Unlocks.Senses, Unlocks.Speed, Unlocks.Sunflowers, 
            Unlocks.Trees, Unlocks.Utilities, Unlocks.Variables, Unlocks.Watering
        ]
        
        is_till = False
        
        # Get world size
        n = get_world_size()
        
        # System Preference
		#start_benchmark_time = get_time()
        #start_benchmark_op_count = get_op_count()
        #set_farm_size(n)
        #set_execution_speed(-1)

		max_n_items = {
			"cactus": 10000
		}

        # Running to all the square in the grid
        for pos in range(n * n):
            x = pos // n
            y = pos % n
            
            # Move to the target direction
            move_to_target(x, y)
            
            #trade(items["dinosaur_egg"], 100)
            
            # Trading    
            trade_item(items["carrot_seed"], items["pumpkin_seed"], items["sunflower_seed"], items["fertilizer"], items["barrel"], items["cactus_seed"], items["dinosaur_egg"])
            
            # Perform the actions in different ground types
            if get_ground_type() == Grounds.Turf:
                if plant_turf(entities["bush"], entities["tree"], entities["grass"], items["fertilizer"]):
                    break
            elif get_ground_type() == Grounds.Soil:
                if plant_soil(sunflower_list, entities["carrot"], entities["pumpkin"], entities["sunflower"], items["water_barrel"], entities["cactus"], items["dinosaur_egg"], n):
                    is_till = True
                    break
               
            unlock_system(unlock_items)
              
        if is_till:
            till_all()
            reset_pos()
            
        #end_benchmark_time = get_time() - start_benchmark_time
		#end_benchmark_op_count = get_op_count() - start_benchmark_op_count
		
		#print("Ending benchmark time", end_benchmark_time, "seconds and ending benchmark op count at" , end_benchmark_op_count)

main()
