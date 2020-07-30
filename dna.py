dna_array = "ATTAACGCC"
entrada = dna_array

reverse_dict = {
  "A": "T",
  "T": "A",
  "C": "G",
  "G": "C"
}


dna_array = dna_array[::-1]
#print(thisdict)

result = []
for letter in dna_array:
    result.append(reverse_dict.get(letter))


print("entrada:",entrada)
print("saida:",result)
#return result
