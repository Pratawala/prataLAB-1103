def dictionary(id_number):
    dictionary= {
        "1001":"[watches,10]",
        "1002":"[pc,20]"
    }

    print(dictionary[id_number])


def toture_chamber():
    while True:
        print("owie you are hurting me UwU")



def open_file():
    file = open('message.txt', "w")
    print(file.write("hello"))


def traffic_light(colour):
    colour = colour.read().lower()
    for i in range (11):
        if colour.lower() == "green":
            print("Go",i,"Seconds")

        elif colour.lower() == "yellow":
            print("Slowdown",i, "Seconds")

        elif colour.lower() == "red":
            print("Stop",i, "Seconds")

        


###------------EXECUTION AREA------------###


traffic_light(colour = open("traffic_light.txt", "r"))