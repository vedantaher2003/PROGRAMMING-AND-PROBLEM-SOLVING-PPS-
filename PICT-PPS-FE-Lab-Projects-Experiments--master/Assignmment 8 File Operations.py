'''
Write a program in Python to count total characters in file, total
words in file, total lines in file and frequency of given word in file.
'''
search=input("Enter the word to be searched:")
file=open("input.txt","r")
characters=0
words=0
total_lines=0
frequency=0
for line in file:
    total_lines+=1
    if search in line:
        frequency+=1
    words_list=line.split()
    words+=len(words_list)
    for i in words_list:
        characters+=len(i)
print("Total Characters:",characters)
print("Total Words:",words)
print("Total Lines:",total_lines)
print("Frequency of {} is".format(search),frequency)
file.close()


