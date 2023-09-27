print('Hellowork干1234')
#str = input("请输入：")
#print("你输入的内容是: ", str)
fo = open("foo.txt", "r+")
#fo.write( "www.runoob.com!\nVery good site!\n")
print("文件名: ", fo.name)
#print "是否已关闭 : ", fo.closed
#print "访问模式 : ", fo.mode
line = fo.readline()
print("读取第一行 %s" % (line))
line = fo.readline(5)
print("读取第一行 %s" % (line))
fo.close()
