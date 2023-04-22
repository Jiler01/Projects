def collide(obj1,obj2):
    x1_1 = obj1.x
    y1_1 = obj1.y

    x2_1 = obj1.x + obj1.w
    y2_1 = obj1.y + obj1.h


    x1_2 = obj2.x
    y1_2 = obj2.y

    x2_2 = obj2.x + obj2.w
    y2_2 = obj2.y + obj2.h

    notX = x1_1 > x2_2 or x1_2 > x2_1
    notY = y1_1 > y2_2 or y1_2 > y2_1

    return not (notX or notY)