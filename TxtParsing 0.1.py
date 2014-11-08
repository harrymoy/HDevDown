def returnLink(href):
	return "<a href="+href+">"

def returnHeader(n, text):
	return "<h"+ n + ">" + text + "</h" + n + ">"

def returnBody(body):
	return "<p>" + body + "</p>"

question = raw_input("Do you want a link? y/n")
linkTitle=""
if question == "y":
	link = raw_input("Enter link")
	linkTitle = returnLink(link)

while True:
	fileName = raw_input("file name")
	try:
		file = open(fileName, 'r')
		break
	except(FileNotFoundError):
		print "File not found"


# lines = file.readLines()
output=""
for i in file:
	i=i.strip()
	if i[0] == "#":
		text = i[2:]
		n = i[1]
		output+=returnHeader(n, text)+"\n"

	else:
		body = i
		output+=returnBody(body)


print output
