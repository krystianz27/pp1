text = "Forests cover about 30,5% of Poland's land area based on international standards. Its overall percentage is still increasing. Forests of Poland are managed by the national program of reforestation (KPZL), aiming at an increase of forest-cover to 33% in 2050. The richness of Polish forest (per SoEF 2011 statistics) is more than twice as high as European average (with Germany and France at the top), containing 2.304 billion cubic metres of trees. The largest forest complex in Poland is Lower Silesian Wilderness. More than 1% of Poland's territory, 3,145 square kilometres (1,214 sq mi), is protected within 23 Polish national parks. Three more national parks are projected for Masuria, the Polish Jura, and the eastern Beskids. In addition, wetlands along lakes and rivers in central Poland are legally protected, as are coastal areas in the north. There are over 120 areas designated as landscape parks, along with numerous nature reserves and other protected areas (e.g. Natura 2000)."

# a.	All words ‘Poland’
# b.	Country names (Poland, Germany and France)
# c.	Punctuation marks (dots and commas)
# d.	Numbers representing a year (four-digit numbers)
# e.	Capital letters
# f.	Vowels
# g.	Words with at least five letters.
# h.	Words starting with capital letters

import re



# print(re.findall("Poland", text)) #a

# print(re.findall("Poland|Germany|France", text)) #b

# print(re.findall("\.|,", text)) #c

# print(re.findall("[1-9][0-9][0-9][0-9]", text)) #d

# print(re.findall("[A-Z]", text)) #e

# print(re.findall("[aeiou]", text)) #f


# x = (re.findall(r"\w+", text))  #g

# def filter_word(n):
#     if len(n) >=5:
#         return True
#     else:
#         return False

# list = list(filter(filter_word, x))
# print(list)


list = re.findall(r"\w+", text)  #g
list2 = []
for word in list:
    if len(word) >= 5:
        list2.append(word)
print(list2)



# print(re.findall(r"\b[A-Z]\w+", text)) #h 






