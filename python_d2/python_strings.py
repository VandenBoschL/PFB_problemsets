#!/usr/bin/env python3

# Split a string into a list

taxa = 'sapiens, erectus, neanderthalensis'
print(taxa)
print(taxa[1])
species =  taxa.split(", ")
print(species)

print(species[1])
species_sorted = sorted(species,key=len)
print(species_sorted)
