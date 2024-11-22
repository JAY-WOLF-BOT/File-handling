file_read = open('Codingal.txt','r')
print("File in Read Mode - ")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt','w')
file_write.write(" File in write mode....")
file_write.write("Hi! I am penguin. I am 1 yr old")
file_write.close()

file_write = open('Codingal.txt','a')
file_write.write("\n File in append mode....")
file_write.write("Hi! I am penguin. I am 1 yr old")
file_write.close()
