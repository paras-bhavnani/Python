sampleData = "Hi everyone! My name is Paras Bhavnani. "

newFile = open('sampleData.text',"w+")
newFile.write(sampleData)
newFile.close()

readFile = open('sampleData.text',"r")
oldData = readFile.read()
print(oldData)
readFile.close()
newData = "This is something more than before"

appendFile = open('sampleData.text',"a+")
appendFile.write(newData)