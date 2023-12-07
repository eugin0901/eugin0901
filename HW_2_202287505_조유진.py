first_set = set(eval(input("Enter the fist set:")))
second_set = set(eval(input("Enter the sencond set:")))

jaccard_similarity_coefficient = len(first_set.intersection(second_set)) / len(first_set.union(second_set))
print("jaccard_similarity_coefficient is {:.3f}".format(jaccard_similarity_coefficient))
