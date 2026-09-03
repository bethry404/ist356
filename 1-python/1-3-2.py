def cleanup(text) -> str:
    """txt = text.strip(" ").lower().replace("!", "").replace(",", "").replace(".", "").replace("?", "")
    return txt"""

    text2 = text
    for char in ["!", ",", ".", "?"]:
        text2 = text2.replace(char, "")
    text3 = text2.strip()
    text4 = text3.lower()
    return text4

# test function with a couple of calls






result = cleanup(input("Enter a string: "))
print(result)