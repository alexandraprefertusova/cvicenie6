from circle_stats import has_intersection
from circles_intersection_draw import draw_data

def main():

    circle_1 = {"x": 0, "y": 0, "r": 3}
    circle_2 = {"x": 4, "y": 0, "r": 2}


    result = has_intersection(circle_1, circle_2)


    if result["is_intersection"]:
        print(f"Kružnice se protínají a mají {result['intersections_count']} průniky/průnik.")
    else:
        print("Kružnice se neprotínají.")


    print("Otevírám okno s grafem...")
    draw_data(circle_1, circle_2)

if __name__ == "__main__":
    main()

