def area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def is_non_degenerate(x1, y1, x2, y2, x3, y3):
    return area(x1, y1, x2, y2, x3, y3) != 0

def is_point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    total_area = area(x1, y1, x2, y2, x3, y3)

    area1 = area(px, py, x2, y2, x3, y3)
    area2 = area(x1, y1, px, py, x3, y3)
    area3 = area(x1, y1, x2, y2, px, py)
    return total_area == area1 + area2 + area3

def determine_scenario(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    if not is_non_degenerate(x1, y1, x2, y2, x3, y3):
        return 0  

    p_in_triangle = is_point_in_triangle(xp, yp, x1, y1, x2, y2, x3, y3)
    q_in_triangle = is_point_in_triangle(xq, yq, x1, y1, x2, y2, x3, y3)

    if p_in_triangle and not q_in_triangle:
        return 1  
    elif q_in_triangle and not p_in_triangle:
        return 2  
    elif p_in_triangle and q_in_triangle:
        return 3  
    else:
        return 4

print(determine_scenario(2,2,7,2,5,4,4,3,7,4)) #1
print(determine_scenario(0,0,2,0,4,0,2,0,4,0)) #0  
