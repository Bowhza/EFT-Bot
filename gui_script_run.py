import logging
import threading
import argparse
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

# Argument parser setup
parser = argparse.ArgumentParser(description="Run the bot script with map, heal, and skill options.")

parser.add_argument("--map", required=True, help="Specify the map to run.")
parser.add_argument("--heal", required=True, help="Specify the healing option.")
parser.add_argument("--skill", required=True, help="Specify the skill to train.")

args = parser.parse_args()

# Map options with logging
maps = {
    "Shoreline": lambda: (logging.info("Running Shoreline"), select_map.run_map("shoreline", scale_factor)),
    "Woods": lambda: (logging.info("Running Woods"), select_map.run_map("woods", scale_factor)),
    "Customs": lambda: (logging.info("Running Customs"), select_map.run_map("customs", scale_factor)),
    "Factory": lambda: (logging.info("Running Factory"), select_map.run_map("factory", scale_factor)),
    "Interchange": lambda: (logging.info("Running Interchange"), select_map.run_map("interchange", scale_factor)),
    "Lighthouse": lambda: (logging.info("Running Lighthouse"), select_map.run_map("lighthouse", scale_factor)),
    "Reserve": lambda: (logging.info("Running Reserve"), select_map.run_map("reserve", scale_factor)),
    "Streets Of Tarkov": lambda: (logging.info("Running Streets Of Tarkov"), select_map.run_map("streets", scale_factor)),
    "Ground Zero": lambda: (logging.info("Running Ground Zero"), select_map.run_map("groundzero", scale_factor))
}

# Healing options with logging
health = {
    "Full heal": lambda: (logging.info("Applying Full Heal"), heal.fullheal.heal(scale_factor=scale_factor)),
    "Only heal breaks and bleeds": lambda: (logging.info("Applying Only Heal Breaks and Bleeds"), 
                                            heal.nohpheal.heal(scale_factor=scale_factor)),
    "Don't heal": lambda: (logging.info("Not Healing"), heal.noheal.heal(scale_factor=scale_factor))
}

# Skill options with logging
skills = {
    "Endurance/strength": lambda: (logging.info("Training Endurance/Strength"),
                                    skill.endurance.run(scale_factor)),
    "Covert": lambda: (logging.info("Training Covert"), skill.covert.run())
}


# Validation for argument inputs
def validate_arguments():
    if args.map not in maps:
        logging.error(f"Invalid Map Selected: {args.map}")
        raise ValueError(f"Invalid Map: {args.map}")
    if args.heal not in health:
        logging.error(f"Invalid Healing Option Selected: {args.heal}")
        raise ValueError(f"Invalid Healing Option: {args.heal}")
    if args.skill not in skills:
        logging.error(f"Invalid Skill Selected: {args.skill}")
        raise ValueError(f"Invalid Skill: {args.skill}")


def main():
    # Validate the arguments
    try:
        validate_arguments()
    except ValueError as e:
        logging.error(f"Validation Error: {e}")
        return

    # Select options based on the args
    map_selection = maps[args.map]
    healing_option = health[args.heal]
    skill_option = skills[args.skill]

    # Create threads
    map_thread = threading.Thread(target=map_selection, name="MapThread")
    heal_thread = threading.Thread(target=healing_option, name="HealThread")
    skill_thread = threading.Thread(target=skill_option, name="SkillThread")

    # Start the threads
    map_thread.start()
    heal_thread.start()
    skill_thread.start()

    # Wait for threads to complete
    map_thread.join()
    heal_thread.join()
    skill_thread.join()

if __name__ == "__main__":
    main()
