def collide(obj1,obj2):
    if abs(obj1.x - obj2.x) < obj1.w/2+obj2.w/2 and abs(obj1.y - obj2.y) < obj1.h/2+obj2.h/2:
        return True
    return False