def collide(rect1, rect2):
    # Coordonnées des coins supérieur gauche et inférieur droit des rectangles
    rect1_coords = (rect1.x, rect1.y, rect1.x + rect1.w, rect1.y + rect1.h)
    rect2_coords = (rect2.x, rect2.y, rect2.x + rect2.w, rect2.y + rect2.h)

    # Vérification de la collision selon l'axe x
    x_overlap = not (rect1_coords[2] < rect2_coords[0] or rect2_coords[2] < rect1_coords[0])

    # Vérification de la collision selon l'axe y
    y_overlap = not (rect1_coords[3] < rect2_coords[1] or rect2_coords[3] < rect1_coords[1])

    # Si les deux conditions sont vraies, les rectangles se chevauchent
    return x_overlap and y_overlap