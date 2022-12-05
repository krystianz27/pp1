def f(human_age):
    human_age = int(human_age)

    if human_age >=2:
        dog_age = 20 + (human_age-2)*4
        return dog_age
    elif human_age >= 0 and human_age < 2:
        dog_age = human_age*10
        return dog_age



# print(f(15))
# print(f(2))