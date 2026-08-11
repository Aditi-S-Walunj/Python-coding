a=input("Enter string:")
count=sum(1 for ch in a.lower() if ch in "aeiou")
print("Vowels:",count)