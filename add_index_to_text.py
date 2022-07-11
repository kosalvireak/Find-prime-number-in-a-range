file = open('python_question.txt', 'r')
file1 = open('python_questions.txt', 'a')
i = 1
for each in file:
    file1.write("%d.  %s"%(i,each))
    #print ("%d.  %s"%(i,each))
    i = i + 1