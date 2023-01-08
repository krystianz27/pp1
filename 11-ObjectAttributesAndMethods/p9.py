class Arrays():

    @staticmethod
    def numbers(number_of_array_elements, value_of_array_elements):
        array = []
        for x in range(number_of_array_elements):
            array.append(value_of_array_elements)
        return array


    @staticmethod
    def random_value(number_of_elements, m,n):
        from random import randint
        array = []
        for x in range(number_of_elements):
            array.append(randint(m,n))
        return array


    @staticmethod
    def elements (array, value_from, value_to):
        count = 0
        for x in array:
            if x >= value_from and x <= value_to:
                count +=1
        return count



print(Arrays.numbers(5, 3))

print(Arrays.random_value(10, 0, 100))

array = [2,3,43,5,432,43,24,56]
print(Arrays.elements(array, 10, 100))
