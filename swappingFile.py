def swapFileData() : 
    fileName = input("Enter the name of the first file : ")
    file2Name = input("Enter the name of the second file : ")
     #file1Data = open(fileName, 'r+')
     #file2Data = open(file2Name, 'r+')

     #file1Data = open(file2Data)
     #savedData = open(file1Data)
    with open(fileName, 'r') as a : 
        data_a = a.read()

    with open(file2Name, 'r') as b : 
        data_b = b.read()

    with open(fileName, 'w') as a : 
        a.write(data_b)

    with open(file2Name, 'w') as b : 
        b.write(data_a)

swapFileData()