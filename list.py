numbers = [-5, 3, 0, -1, 7, 8, -2]

positive_numbers = [num for num in numbers if num > 0]

print(positive_numbers)

n = 5

squares = [x**2 for x in range(1, n + 1)]

print(squares)

word = "nandana"

vowels = [char for char in word if char.lower() in 'aeiou']

print(vowels)

line = input("Enter a line of text: ")

# Split line into words, then for each word create a list of ordinals of its characters
ordinals_per_word = [[ord(char) for char in word] for word in line.split()]

print(ordinals_per_word)
