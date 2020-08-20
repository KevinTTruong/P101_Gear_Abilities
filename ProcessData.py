class ProcessData:
    def __init__(self, filename):
        self.powers = {
            "Buccaneer": set(),
            "Swashbuckler": set(),
            "Privateer": set(),
            "Musketeer": set(),
            "Witchdoctor": set(),
            "All Classes": set()
        }
        self.data = open("Gear.txt", "r")
        self.index_text = "Gives Ability: "
        self.__process()
        self.__output()

    # For each line/piece of gear, get the ability(ies) and place
    # them in the corresponding class's list of abilities.
    def __process(self):
        line = self.data.readline()
        while line != "":
            clas = self.__find_class(line)
            if self.index_text in line and clas != "":
                ability = line[line.index(self.index_text)+len(self.index_text):line.index("\n")]

                # Filter credits and boss drop notes
                if ' -' in ability:
                    ability = ability[:ability.index(' -')]
                if ' *' in ability:
                    ability = ability[:ability.index(' *')]

                # Splits abilities where the gear gives 2 abilities,
                # otherwise add the ability onto list.
                if ' & ' in ability:
                    ability1 = ability[:ability.index(' &')]
                    ability2 = ability[ability.index('& ')+len('& '):]
                    self.powers[clas].add(ability1)
                    self.powers[clas].add(ability2)
                elif ' and ' in ability:
                    ability1 = ability[:ability.index(' and')]
                    ability2 = ability[ability.index('and ')+len('and '):]
                    self.powers[clas].add(ability1)
                    self.powers[clas].add(ability2)
                else:
                    self.powers[clas].add(ability)

            # Iterate to next line
            line = self.data.readline()
        self.__sort_powers()
        self.data.close()

    # Determine the class of the gear given the whole line.
    def __find_class(self, line):
        if "Buccaneer" in line:
            return "Buccaneer"
        elif "Swashbuckler" in line:
            return "Swashbuckler"
        elif "Privateer" in line:
            return "Privateer"
        elif "Musketeer" in line:
            return "Musketeer"
        elif "Witchdoctor" in line:
            return "Witchdoctor"
        elif "All Classes" in line:
            return "All Classes"
        else:
            return ""

    # Sort each class's list of abilities in alphabetical order.
    def __sort_powers(self):
        for key in self.powers:
            self.powers[key] = sorted(self.powers[key])

    # Write 6 separate files for each class.
    def __output(self):
        for key in self.powers:
            out = open("Gear Powers by Class/"+key+".txt", "w")

            # Prints out each ability in a new line
            for ability in self.powers[key]:
                out.write(ability+"\n")

            # Prints abilities accessible by all classes (no repeats)
            if key != "All Classes":
                out.write("\nAll Classes:\n")
                for ability in self.powers["All Classes"]:
                    if ability not in self.powers[key]:
                        out.write(ability+"\n")
            out.close()

    # Used for debugging.
    def print_powers(self):
        for key in self.powers:
            print(self.powers[key])


ProcessData("Gear.txt")
