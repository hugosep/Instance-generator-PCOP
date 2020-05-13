# name files
names = ["1", "2", "3", "4"]

for name in names:
    file = open(name + ".txt", "r")
    lines = file.readlines()

    output = open("output"+name+".txt", "w")

    i = 0

    for line in lines:

        if i == 1:
            line = line.strip()
            line = line.split(" ")
            parallel = line[0]
            output.write("# PARALLEL SESSIONS\n")
            output.write(parallel + "\n\n")

        elif i == 4:
            line = line.strip()
            line = line.split("\t")
            talks = line[-1]
            output.write("# NUMBER OF TALKS\n")
            output.write(str(talks) + "\n\n")
            output.write("# PREFERENCES\n")

        elif i >= 5:
            line = line.strip()
            line = line.split("\t")
            id = line[0]
            output.write(id)
            line = line[1:]

            for j in range(len(line)):
                if int(line[j]) == 1:
                    output.write("\t" + str(j+1))

            output.write("\n")

        i += 1

    file.close()
    output.close()