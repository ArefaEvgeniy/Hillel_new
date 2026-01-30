text = "My name is {}. I live in {}. I am {} years old. {} is a good name."
text_2 = "My name is {0}. I live in {1}. I am {2} years old. {0} is a good name."
text_3 = "My name is {name}. I live in {city}. I am {years} years old. {name} is a good name."

name = "Alice"
city = "Wonderland"
age = 10
age_2 = 34

print(text.format(name, city, age, name, 'RRR'))
print(text.format('John', 'Ney York', age_2, 'John'))

print(text_2.format(name, city, age, 'RRR', 'TTT'))
print(text_3.format(city=city, name=name, years=age))
