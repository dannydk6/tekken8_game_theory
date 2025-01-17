import argparse
from tekken8_game_theory.xlsx import full_run

def print_scenarios(run):
    for r in run:
        for k, v in r['metadata'].items():
            print(k, ': ', v)
        print()
        print(r['df'])
        print()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run GTO Distributions for a given character")
    parser.add_argument("-n", "--name", default='reina', type=str, required=False, help="Name of the character")

    # Parse the argument
    args = parser.parse_args()

    character = args.name
    base_path = f"data/{character}"

    run = full_run(f"{character}_gto.xlsx", 
            f"{base_path}/inputs",
            f"{base_path}/artifacts",
            output_dir=f"{base_path}/output", 
            precision=0, 
            drop_zeros=True)

    print(f'\n{character} Scenarios\n')

    print_scenarios(run)

# Run the script only if it's executed directly
if __name__ == "__main__":
    main()