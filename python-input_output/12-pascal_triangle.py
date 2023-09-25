#!/usr/bin/python3
""" shebang """


def pascal_triangle(n):
    """
    Generate Pascal's triangle with n rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        None.

    Examples:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        >>> pascal_triangle(0)
        []

    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                element = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(element)
        triangle.append(row)

    return triangle
