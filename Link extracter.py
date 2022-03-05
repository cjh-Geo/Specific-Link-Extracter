while True:
    e = 0
    words = ""
    while True:
        line = input()
        words += line
        if line == "				<!-- END OF ACCOMMODATION SECTION -->": #Check if end of input (for multiple lines), change to end of your input
            print("done")
            break
    iden = words.split("?")
    for x in range(0, len(iden)):
        iden[x] = iden[x].split('/')
    chained = []
    while iden:
            chained.extend(iden.pop(0))

    iden = chained

    for x in range(0, len(iden)):
        iden[x] = iden[x].split('"')
    chained = []
    while iden:
            chained.extend(iden.pop(0))

    iden = chained

    link = ""
    aftx = 0
    for x in range(0, len(iden)):
        if iden[x] == "tour-info": #change "tour-info" to what the specific keyword you are looking for in your link
            aftx = x + 1
            link1 = link
            link = "https://tdi.sg/" + str(iden[x]) + "?" + str(iden[aftx]) # Add or take out depending on how your link is split, if split into more parts consider adding aftx1, aftx2 etc.
            if link!= link1:
                print(link)
