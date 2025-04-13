def uncommon_chars(s1, s2):
    """
    Returns a string consisting of characters that are in s1 or s2 but not in both.
    """
    set1 = set(s1)
    set2 = set(s2)
    common = set1 & set2
    result = ''.join(ch for ch in s1 if ch not in common) + \
             ''.join(ch for ch in s2 if ch not in common)
    return result

ans = ""
with open("chalkboardgag.txt") as f:
    lines = f.readlines()
    for line in lines:
        # Only process lines that deviate from the reference string.
        if line.strip() != "I WILL NOT BE SNEAKY":
            ans += uncommon_chars(line, "I WILL NOT BE SNEAKY").strip()

# Output the flag in picoCTF{...} format.
print("picoCTF{" + ans + "}")
