import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S", handlers=
                    [
                        logging.FileHandler("details.log"),
                        logging.StreamHandler()
                    ])

import skill.endurance
import skill.covert
import skill.death
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


maps = [
    ["Shoreline", map.shoreline.run],
    ["Woods", map.woods.run],
    ["Customs", map.customs.run],
    ["Factory", map.factory.run],
    ["Interchange", map.interchange.run],
    ["Lighthouse", map.lighthouse.run],
    ["Reserve", map.reserve.run],
    ["Streets Of Tarkov", map.streets.run],
]


def main():
    print("What map do you want to run?")

    for index, ctx in enumerate(maps):
        print("{} - {}".format(index, ctx[0]))

    maps_index = int(input("Your map choice: "))
    maps[maps_index][1]()


if __name__ == "__main__":
    main()

health = [
    ["Full heal", heal.fullheal.run],
    ["Only heal breaks and bleeds", heal.nohpheal.run],
    ["Don't heal", heal.noheal.run],

]


def main():
    print("How would you like to heal upon death?")

    for index, ctx in enumerate(health):
        print("{} - {}".format(index, ctx[0]))

    health_index = int(input("Your heal choice: "))
    health[health_index][1]()


if __name__ == "__main__":
    main()



skills = [
    ["Endurance/strength", skill.endurance.run],
    ["Covert", skill.covert.run],
    ["Death, heavy bleed required", skill.death.run],

]


def main():
    print("what skills do you want to level?")

    for index, ctx in enumerate(skills):
        print("{} - {}".format(index, ctx[0]))

    skills_index = int(input("Your skill choice: "))
    skills[skills_index][1]()


if __name__ == "__main__":
    main()