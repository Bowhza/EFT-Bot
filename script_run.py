import logging
import threading
import select_map
import skill.endurance
import skill.covert
import heal.noheal
import heal.nohpheal
import heal.fullheal

from tools.image_scale import get_scale_factor

scale_factor = get_scale_factor()

# Setup logging
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] [%(levelname)s] - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    handlers=[
                        logging.FileHandler("details.log"),
                        logging.StreamHandler()])

# Map options with debug logging inside lambdas
maps = [
    ["Shoreline", lambda: (logging.info("Running Shoreline"), select_map.run_map("shoreline", scale_factor))],
    ["Woods", lambda: (logging.info("Running Woods"), select_map.run_map("woods", scale_factor))],
    ["Customs", lambda: (logging.info("Running Customs"), select_map.run_map("customs", scale_factor))],
    ["Factory", lambda: (logging.info("Running Factory"), select_map.run_map("factory", scale_factor))],
    ["Interchange", lambda: (logging.info("Running Interchange"), select_map.run_map("interchange", scale_factor))],
    ["Lighthouse", lambda: (logging.info("Running Lighthouse"), select_map.run_map("lighthouse", scale_factor))],
    ["Reserve", lambda: (logging.info("Running Reserve"), select_map.run_map("reserve", scale_factor))],
    ["Streets Of Tarkov", lambda: (logging.info("Running Streets Of Tarkov"), select_map.run_map("streets", scale_factor))],
    ["Ground Zero", lambda: (logging.info("Running Ground Zero"), select_map.run_map("groundzero", scale_factor))],
]

# Healing options wrapped in lambdas
health = [
    ["Full heal", lambda: (logging.info("Applying Full Heal"), heal.fullheal.heal(scale_factor=scale_factor))],
    ["Only heal breaks and bleeds",
     lambda: (logging.info("Applying Only Heal Breaks and Bleeds"),
              heal.nohpheal.heal(scale_factor=scale_factor))],
    ["Don't heal", lambda: (logging.info("Not Healing"), heal.noheal.heal(scale_factor=scale_factor))],
]

# Skill options wrapped in lambdas
skills = [
    ["Endurance/strength", lambda: (logging.info("Training Endurance/Strength"),
                                    skill.endurance.run(scale_factor))],
    ["Covert", lambda: (logging.info("Training Covert"), skill.covert.run())],
]


# Function to display options and return the selected lambda or function
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


def main():
    # Map selection
    map_choice = choose_option(maps, "map")

    # Healing selection
    healing_choice = choose_option(health, "healing option")

    # Skill selection
    skill_choice = choose_option(skills, "skill")

    # Create the threads for each method
    map_thread = threading.Thread(target=map_choice, name="MapThread")
    heal_thread = threading.Thread(target=healing_choice, name="HealThread")
    skill_thread = threading.Thread(target=skill_choice, name="SkillThread")

    # Start the threads
    map_thread.start()
    heal_thread.start()
    skill_thread.start()

    # Join the threads to ensure they complete before exiting
    map_thread.join()
    heal_thread.join()
    skill_thread.join()


if __name__ == "__main__":
    main()
