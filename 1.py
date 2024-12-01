def part1() :

    list1 = []
    list2 = []
    total = 0
    file = open("1.txt", "r")

    for line in file:
        splitLine = line.split("   ")
        list1.append(splitLine[0])
        list2.append(splitLine[1])

    list1.sort()
    list2.sort()


    for i in range(0, len(list1)):
        temp = abs(int(list1[i]) - int(list2[i]))
        total += temp

    print(total)

def part2() :
    list1 = []
    list2 = []
    similarityScore = 0
    file = open("1.txt", "r")

    for line in file:
        splitLine = line.split("   ")
        list1.append(int(splitLine[0]))
        list2.append(int(splitLine[1]))

    list1.sort()
    list2.sort()

    for num in list1:
        count = list2.count(num)
        similarityScore += num * count

    print(similarityScore)

part2()