n = int(input())
cities_coordinate = list(map(int, input().split(" ")))

city_cost_final = []
for city_index, city_coordinate in enumerate(cities_coordinate):
    if city_index == (n-1):
        city_cost_final.append([abs(city_coordinate -
                                    cities_coordinate[n-2]),
                                abs(city_coordinate - cities_coordinate[0])])
    elif city_index == 0:
        city_cost_final.append([abs(city_coordinate -
                                    cities_coordinate[1]),
                                abs(city_coordinate - cities_coordinate[n-1])])
    else:
        city_cost_final.append([min(abs(city_coordinate -
                                        cities_coordinate[city_index-1]), abs(city_coordinate -
                                                                              cities_coordinate[city_index+1])),
                                max(abs(city_coordinate - cities_coordinate[n-1]), abs(city_coordinate - cities_coordinate[0]))])

for final_list in city_cost_final:
    print(*final_list)
