from tekken8_game_theory.xlsx import full_run

base_path = "data/reina"

full_run("reina_gto.xlsx", 
         f"{base_path}/inputs",
         f"{base_path}/artifacts",
         output_dir=f"{base_path}/output", 
         precision=0, 
         drop_zeros=True)