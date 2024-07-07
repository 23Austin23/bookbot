def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        numWords = countWords(file_contents.split())
        charsCount = countChars(file_contents.split())
        charsCount.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {path} ---")
        print(f"{numWords} words found in the document", end="\n\n\n")
        for item in charsCount:
            char = item["name"]
            nums = item["num"]
            print(f"The '{char}' character was found {nums} times")
        print("--- End report ---")

def countWords(content):
    num = 0
    for word in content:
        num += 1
    return num 

def countChars(content):
    count = []
    for word in content:
        for char in word:
            char = char.lower()
            found = False
            for item in count:
                found = False
                if item["name"] == char:
                    item["num"] += 1
                    found = True
                    break
            if not found:
                count.append({"name": char, "num": 1})            
    return count

def sort_on(dict):
    return dict["num"]


main()