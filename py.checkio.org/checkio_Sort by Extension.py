"""
You are given a list of files. You need to sort this list by the file extension. The files with the same extension (or without one) should be sorted by name.
Some possible cases:
Filename cannot be an empty string;
Sorting order: files without name, files without extension, files with name and extension;
Filename .config or config. is all name with an empty extension;
Filename like str1.str2.str3 has an extension str3 and a name str1.str2;
Filename like .str1.str2 has an extension str2 and a name .str1.
Input: List of strings.
Output: List of strings.
"""
def sort_by_ext(files: list[str]) -> list[str]:
    return sorted(files, key=sort_key)


def sort_key(file) -> tuple[str, str]:
    name, dot, ext = file.rpartition(".")
    return (("", ext), (ext, name))[bool(name)]


files = [".dat", "1.cad", "1.bat", "1.aa", ".a.a.doc", "slovo"]
res = sort_by_ext(files)
print(res)