Prienik kružníc – Python projekt

Tento program zisťuje, či sa dve kružnice pretínajú a koľko majú prienikov (0, 1 alebo 2). Zároveň vypíše výsledok do terminálu a vykreslí kružnice do grafu.

Štruktúra projektu

Projekt obsahuje tieto súbory:

circle_stats.py
Modul s matematickými funkciami:

radius_sum(r1, r2) – vráti súčet polomerov.

euclid_distance(x1, y1, x2, y2) – vypočíta Euklidovskú vzdialenosť medzi dvoma bodmi.

has_intersection(circle_1, circle_2) – zistí, či sa kružnice pretínajú a koľko majú prienikov.

circle_intersection.py
Hlavný skript programu:

definuje dve kružnice ako slovníky (x, y, r),

zavolá funkciu has_intersection,

vypíše výsledok do terminálu.

circles_intersection_draw.py
Obsahuje funkciu draw_data(circle_1, circle_2), ktorá vykreslí kružnice pomocou knižnice matplotlib.

Reprezentácia kružnice

Kružnica je uložená ako slovník:
circle = {"x": 0, "y": 0, "r": 2}
x, y – súradnice stredu

r – polomer kružnice

Výstup funkcie

Funkcia has_intersection() vracia slovník napríklad:

{
    "is_intersection": True,
    "intersections_count": 2
}
Inštalácia knižnice

Na vykreslenie grafu je potrebná knižnica matplotlib:
(nahlad grafu : ![Figure_1.png](../../Figure_1.png)

uv add matplotlib
Spustenie programu

Program spustíš príkazom:

python circle_intersection.py

Program vypíše informáciu o prieniku kružníc a zobrazí ich v grafe.