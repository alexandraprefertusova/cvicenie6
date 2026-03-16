import math


def radius_sum(r1, r2):

    return r1 + r2


def euclid_distance(x1, y1, x2, y2):

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def has_intersection(circle_1, circle_2):

    d = euclid_distance(circle_1['x'], circle_1['y'], circle_2['x'], circle_2['y'])
    r_sum = radius_sum(circle_1['r'], circle_2['r'])
    r_diff = abs(circle_1['r'] - circle_2['r'])


    result = {"is_intersection": False, "intersections_count": 0}


    if d > r_sum:
        return result


    elif math.isclose(d, r_sum):
        result.update({"is_intersection": True, "intersections_count": 1})


    elif d < r_diff:
        return result


    elif math.isclose(d, r_diff):
        result.update({"is_intersection": True, "intersections_count": 1})


    elif r_diff < d < r_sum:
        result.update({"is_intersection": True, "intersections_count": 2})

    return result

#testy

import math
from circle_stats import has_intersection


print("TEST 1 – dotyk zvonku (1 prienik)")
circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 4, "y": 0, "r": 2}
print(has_intersection(circle_1, circle_2))
# d = 4, r_sum = 4 → math.isclose(d, r_sum)


print("\nTEST 2 – jedna kružnica je úplne vo vnútri druhej (žiadny prienik)")
circle_1 = {"x": 0, "y": 0, "r": 5}
circle_2 = {"x": 1, "y": 1, "r": 1}
print(has_intersection(circle_1, circle_2))
# d < r_diff


print("\nTEST 3 – vnútorný dotyk (1 prienik)")
circle_1 = {"x": 0, "y": 0, "r": 5}
circle_2 = {"x": 3, "y": 0, "r": 2}
print(has_intersection(circle_1, circle_2))
# d = r_diff → math.isclose(d, r_diff)


print("\nTEST 4 – dva prieniky")
circle_1 = {"x": 0, "y": 0, "r": 3}
circle_2 = {"x": 4, "y": 0, "r": 3}
print(has_intersection(circle_1, circle_2))
# r_diff < d < r_sum


print("\nTEST 5 – žiadny prienik (kružnice sú ďaleko)")
circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 10, "y": 0, "r": 2}
print(has_intersection(circle_1, circle_2))
# d > r_sum