from random import *
import math

# preferences
def generate_preferences(file, assistants, talks):
    for assistant in range(1, assistants + 1):
        preferences = sample(range(1, talks+1), randint(1, talks+1))
        preferences = map(str, preferences)
        preference = "\t".join(preferences)
        file.write(str(assistant) + "\t" + preference + "\n")

    return

# speakers
def generate_speakers_disponibility(file, speakers, sessions):
    file.write("# SPEAKER NO AVAILABILITY\n")

    for speaker in range(1, speakers + 1):
        disponibilities = sample(range(1, sessions+1), randint(1, sessions))
        disponibilities = map(str, disponibilities)
        disponibility = "\t".join(disponibilities)
        file.write(str(speaker) + "\t" + disponibility + "\n")

    file.write("\n")

    return

# size rooms
def generate_size_rooms(file, rooms):
    file.write("# SIZE ROOMS\n")

    for room in range(rooms):
        capacities = random.randint(range(45, 1000), rooms)
        capacities = map(str, capacities)
        capacities = "\t".join(capacities)
        file.write(room + "\t" + capacities + "\n")

    file.write("\n")

    return

# type talks
def generate_type_talks(file, talks, types):
    file.write("# TYPE TALKS\n")

    for talk in range(1, talks+1):
        type_talk = randint(1, types+1)
        file.write(str(talk) + "\t" + str(type_talk) + "\n")

    file.write("\n")

    return

# topic talks
def generate_topic_talks(file, talks, types):
    file.write("# TOPIC TALKS\n")

    for talk in range(1, talks+1):
        topic_talk = randint(1, types+1)
        file.write(str(talk) + "\t" + str(topic_talk) + "\n")

    file.write("\n")

    return

def generate_conflict_talks(file, talks, types):
    file.write("# CONFLICT TYPE TALKS\n")

    for _ in range(randint(0, 2)):
        type_1 = randint(1, types+1)
        type_2 = randint(1, types+1)
        file.write(str(type_1) + "\t" + str(type_2) + "\n")

    return


# con entrada por terminal
"""name_file = input("Nombre archivo: ")
preferences = bool(input("Preferencias?: "))
assistants = int(input("Número de asistentes: "))
talks = int(input("Número de charlas: "))
talks_by_session = int(input("Número charlas por sesión: "))
types = int(input("Número de tipos: "))
sessions = math.ceil(talks / talks_by_session)"""


# parametros por codigo
name_file = "new/output4.txt"
preferences = True
assistants = 104
talks = 80
talks_by_session = 2
types = 3
sessions = math.ceil(talks / talks_by_session)

file = open(name_file, "a+")

# add to preferences
if not preferences:
    generate_preferences(file, assistants, talks)

file.write("\n")

generate_speakers_disponibility(file, talks, sessions)
generate_type_talks(file, talks, types)
generate_topic_talks(file, talks, types)
generate_conflict_talks(file, talks, types)

file.close()
