def sort_dict(dict_of_chars):
    list_dict = []
    for key in dict_of_chars:    
        list_dict.append({"char":key, "num": dict_of_chars[key]})
    #print(list_dict)
    list_dict.sort(reverse = True, key = sort_on)
    return list_dict

def sort_on(dict):
    return dict["num"]    






def count_words(file_content):
    words = file_content.split()
    return len(words)
    # num = 0
    # for i in words:
    #     num += 1
    # return num

def number_of_charecters(file_content):
    result = {}
    for char in file_content:
        lowerKey = char.lower()

        #keyExists = lowerKey in result
        if(lowerKey in result) == False:
            result[lowerKey] = 0
         
        result[lowerKey] += 1

    return result


