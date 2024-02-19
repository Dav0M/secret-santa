import random
import json

from santaMail import *

# Initialize variables
file = 'santaData.json'
unassignedSantas = []
unassignedNames = []


def main():
    global unassignedNames, unassignedSantas

    santaData = load_data(file)
    unassignedSantas = [x for x in santaData]
    unassignedNames = unassignedSantas.copy()

    santaPairs = assign_names(santaData)

    send_emails(santaData, santaPairs)


# Main loop for assigning santas a giftee
def assign_names(santaData):
    santaPairs = {}

    while len(unassignedSantas) > 0:
        santa, candidates = next_santa(santaData)
        giftee = random.choice(candidates)

        santaPairs[santa] = giftee

        unassignedNames.remove(giftee)
        unassignedSantas.remove(santa)

    return santaPairs


# Helper that returns santa with least possible giftees
def next_santa(santaData):
    next = []
    min = float('inf')
    for person in unassignedSantas:
        candidates = [x for x in unassignedNames if x not in santaData.get(person)['exclude'] and x != person]
        if len(candidates) == min:
            next.append((person,candidates))
        elif len(candidates) < min:
            min = len(candidates)
            next = [(person,candidates)]
        else:
            continue

    if min == 0:
        print("Error! Retry the draw or remove some exclusions.")
    return random.choice(next)
    

# Helper to pull data from the json
def load_data(file):
    with open(file, 'r') as f:
        santaData = json.load(f)
    return santaData


# Run main program
if __name__ == "__main__":
    main()