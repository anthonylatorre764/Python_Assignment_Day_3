from math import pi



def square_footage(length, width):
    """
        Calculate the square footage of a rectangular 
        house using the parameters, length and width.
    """
    area = str(length * width) + " square feet"

    return area




def calc_circum(radius):
    """
        Calculate the circumference of a circle
        using radius as the parameter.
    """
    circum = 2*(pi)*radius

    return circum