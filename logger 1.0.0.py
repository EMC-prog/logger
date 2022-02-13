import time
#Logger made by EMC-Prog
print("Logger")
time.sleep(2)
#Now will ask for data
testid = input("Insert ID: ")
test1 = input("Insert comments for test1: ")
test2 = input("Insert comments for test2: ")
other = input("Insert other comments: ")
#Now makes the file
text = '''
<!DOCTYPE html>
<html>
<body>
<h1>Test for ''' + str(testid) + '''</h1>
<hr>
<h2>Test1</h2>
<p>''' + str(test1) + '''</p>
<h2>Test2</h2>
<p>''' + str(test2) + '''</p>
<h2>Other comments</h2>
<p>''' + str(other) + '''</p>
<hr>
<p><b>Created with Logger</b></p>
</body>
</html>
'''
#Now creates the file with the test id
f = open(testid + ".html", "w")
f.write(text)
f.close
exit = input("File created. Thanks for using Logger. Please press enter to exit.")