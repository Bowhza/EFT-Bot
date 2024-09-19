import logging
import map.groundzero
import skill.endurance
import skill.covert
import heal.noheal
import heal.nohpheal
import heal.fullheal
import map.shoreline
import map.customs
import map.factory
import map.interchange
import map.lighthouse
import map.reserve
import map.streets
import map.woods

# Setup logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S", handlers=[
                        logging.FileHandler("details.log"),
                        logging.StreamHandler()
                    ])

# Map options
maps = [
    ["Shoreline", map.shoreline.run],
    ["Woods", map.woods.run],
    ["Customs", map.customs.run],
    ["Factory", map.factory.run],
    ["Interchange", map.interchange.run],
    ["Lighthouse", map.lighthouse.run],
    ["Reserve", map.reserve.run],
    ["Streets Of Tarkov", map.streets.run],
    ["Ground Zero", map.groundzero.run],
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
