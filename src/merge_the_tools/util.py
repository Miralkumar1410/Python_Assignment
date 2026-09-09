def merge_the_tools(string, k):
    results = []

    for i in range(0, len(string), k):
        substring = string[i:i + k]
        result = ""
        seen = set()

        for char in substring:
            if char not in seen:
                result += char
                seen.add(char)

        results.append(result)

    return results