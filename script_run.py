import logging
import select_map
import skill.endurance
import skill.covert
import heal.noheal
import heal.nohpheal
import heal.fullheal


# Setup logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S", handlers=[
                        logging.FileHandler("details.log"),
                        logging.StreamHandler()
                    ])

# Map options
maps = [
    ["Shoreline", lambda: select_map.run_map("shoreline")],
    ["Woods", lambda: select_map.run_map("woods")],
    ["Customs", lambda: select_map.run_map("customs")],
    ["Factory", lambda: select_map.run_map("factory")],
    ["Interchange", lambda: select_map.run_map("interchange")],
    ["Lighthouse", lambda: select_map.run_map("lighthouse")],
    ["Reserve", lambda: select_map.run_map("reserve")],
    ["Streets Of Tarkov", lambda: select_map.run_map("streets")],
    ["Ground Zero", lambda: select_map.run_map("groundzero")],
]

# Healing options
health = [
    ["Full heal", heal.fullheal.run],
    ["Only heal breaks and bleeds", heal.nohpheal.run],
    ["Don't heal", heal.noheal.run],
]

# Skill options
skills = [
    ["Endurance/strength", skill.endurance.run],
    ["Covert", skill.covert.run],
]


# Function to display options and return the selection
def choose_option(options, option_type):
    print(f"Please choose a {option_type}:")
    for index, ctx in enumerate(options):
        print(f"{index} - {ctx[0]}")
    
    while True:
        try:
            choice = int(input(f"Your {option_type} choice: "))
            if 0 <= choice < len(options):
                logging.info(f"Selected {option_type}: {options[choice][0]}")
                return options[choice][1]
            else:
                print("Invalid choice, please enter a valid option.")
        except ValueError:
            print("Please enter a valid number.")


# Main bot logic
def main():
    # Map selection
    map_choice = choose_option(maps, "map")
    
    # Healing selection
    healing_choice = choose_option(health, "healing option")
    
    # Skill selection
    skill_choice = choose_option(skills, "skill")

    # Start bot sequence
    logging.info("Starting the script.")
    map_choice()        # Run the selected map
    healing_choice()    # Apply healing method
    skill_choice()      # Train selected skill


if __name__ == "__main__":
    main()
