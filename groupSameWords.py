# 5. Group Words with Same Letters

# Group words containing the same letters together.

# Input: Array/List of words

# Output: List of groups where each group contains words with same letters


words = ["eat", "tea", "tan", "ate", "nat"]
groups = {}

for word in words:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)

print(list(groups.values()))
