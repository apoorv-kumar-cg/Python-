#Q1
from gettext import find


name="apoorv"
city="gaya"
fav_prog_lang="c++"
message="work smart"

print(name)
print(city)
print(fav_prog_lang)
print(message)

#Q2
a=""
print(a)
print(len(a))
print(type(a))

#Q3
b="Python Programming"
print(b)
print(len(b))
print(b[0])
print(b[17])
print(b[2])
print(b[-2])

#Q4
c="Programming"
print(c[0])
print(c[1])
print(c[4])
print(c[-1])

#Q5
print(c[-1])
print(c[-2])
print(c[-3])
print(c[-11])

#Q6
d="apoorv kumar"
print(d[0])
print(d[-1])
print(d[7])

#Q7
e="Python Programming"
print(e[0:6])
print(e[7:18])
print(e[0:18])
print(e[0:5])
print(e[13:18])

#Q8
f="ABCDEFGHIJKL"
print(f[0:12:2])
print(f[0:12:3])
print(f[1:8:2])
print(f[::-1])

#Q9
g="Python Programming"
print(g)
print(g[-5:])
print(g[-10:])
print(g[-18:])

#Q10
h="abcdefghij"
print(h[0:3])
print(h[7:10])
print(h[0:10:2])
print(h[-10:])
print(h[1:9])

#Q11
word="appli"
sentence="iamhappy"
sentence2="i am happy"
print(len(word))
print(len(sentence))
print(len(sentence2))

#Q12 
i="Python Programming"
print(len(i))

#Q13
first_name="apoorv"
last_name="kumar"
print(first_name + " " + last_name)

#Q14
name="apoorv"
age=20
city="gaya"
programming_language="python"
print("my name is " + name + " and my age is " + str(age) + " and i live in " + city + " and my favourite programming language is " + programming_language)

#Q15
j="Apoorv"
jj=20
print(j+str(jj))

#Q16
k="Python"
print(k*3)
print(k*5)
print(k*10)

#Q17
print("*"*111)

#Q18
l="python programming language"
print(l.upper())
print(l.lower())
print(l.capitalize())
print(l.title())
print(l.swapcase())

#Q19
m="Python"
mm="python"
print(m==mm)
print(m.lower()==mm.lower())

#Q20
n="Python is a programming language"
print("Python" in n)
print("programming" in n)
print("Java" in n)
print("language" in n)

#Q21
print(n.find("Python"))
print(n.find("programming"))
print(n.find("Java"))
print(n.find("language"))   

#Q22
print(n.index("Python"))

#Q23
m="banana"
print(m.count("a"))
print(m.count("n"))
print(m.count("b"))

#Q24
filename = "student_notes.pdf"
print(filename.endswith(".pdf"))
print(filename.startswith("student"))
print(filename.endswith(".txt"))

#Q25
text = "I am learning Java"
print(text.replace("Java", "Python"))

#Q26
text = "apple apple apple"
print(text.replace("apple", "mango"))

#Q27
print(text.replace("apple", "mango", 1))

#Q28
text = "Python"
print(text.upper())

#Q29
text = "   Python Programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Q30

#Q31
n="Python is easy to learn"
print(n.split())

#Q32
a="apple,banana,mango,orange"
print(a.split(","))

#Q33
words=["Python", "is", "easy"]
print(" ".join(words))

#Q34
print("-" .join(words))

#Q35
name="apoorv" 
age=20
city="gaya"
print(f"My name is {name} and I am {age} years old. I live in {city}.")

#Q36
a = 10
b = 20
print(f"The sum is {a + b}.")

#Q37

#A
text = "Python"
print(text[20])

#B
text = "Python"
text[0] = "J"

#C
age = 20
print("Age: " + age)

#D
text = "Python"
print(text.index("Java"))