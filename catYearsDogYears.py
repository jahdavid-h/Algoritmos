''''
Programa que calcula la edad de un gato y un perro
'''

def human_years_cat_dog_years(human_years):
    if human_years == 1:
        catYears = 15
        dogYears = 15
    elif human_years == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (human_years - 2) * 4
        dogYears = 15 + 9 + (human_years - 2) * 5
    return [human_years, catYears, dogYears]

#Ejemplo
test_cases = [1, 2, 3, 5, 10]
results = [human_years_cat_dog_years(human_years) for human_years in test_cases]
print(results)
print(type(results))