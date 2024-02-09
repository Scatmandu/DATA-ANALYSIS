# Read the column.txt file
input_file_path = 'column.txt'

try:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
    exit()

# Count occurrences of each word
word_counts = {}
for line in lines:
    word = line.strip()  # Remove leading/trailing whitespaces
    word_counts[word] = word_counts.get(word, 0) + 1

# Sort the word counts in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Save the sorted word counts to word_count.txt
output_counts_file_path = 'word_count.txt'
with open(output_counts_file_path, 'w', encoding='utf-8') as output_file:
    for word, count in sorted_word_counts:
        output_file.write(f"{word}: {count}\n")

print(f"Word counts saved to '{output_counts_file_path}'.")
