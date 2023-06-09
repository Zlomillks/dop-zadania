def find_country_occurrences():
    countries = []
    line_number = 0

    while True:
        country = input()
        if country == "СТОП":
            break
        countries.append(country)

    country_occurrences = {}
    for i, country in enumerate(countries):
        if country not in country_occurrences:
            country_occurrences[country] = [i]
        else:
            country_occurrences[country].append(i)

    for country, occurrences in country_occurrences.items():
        print(country + ":")
        for occurrence in occurrences:
            print(occurrence)


find_country_occurrences()
