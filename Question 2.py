def find_all(str2,str1):
    length = len(str1)
    c=0
    indexes = []
    while c < len(str2):
        if str2[c:c+length] == str1:
            indexes.append(c)
        c=c+1
    return indexes

find_all("aaaaaddegagagkjfgkhaaaa","aaa")
