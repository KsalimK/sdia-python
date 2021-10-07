def is_unique(x):
<<<<<<< HEAD
    """[summary]

    Args:
        x (list of int]): [the list to test]

    Returns:
        [bool]: [show if there is not 2 same elements in x]
    """
    flag=True
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]==x[j]:
                 flag=False

    return flag

def triangle_shape(height):
    """[summary]

    Args:
        height ([int]): [the height of the triangle]

    Returns:
        [string]:[the triangle of x]
    """

    if height==0:
        return("")
    else:
        r=[(height-i-1)*" "+(2*i+1)*"x"+(height-i-1)*" "  for i in range(height)]



    return("\n".join(r))


# fonctionne à merveille





print(triangle_shape(3))
=======
    """Check that ``x`` has no duplicate elements.

    Args:
        x (list): elements to be compared.

    Returns:
        bool: True if ``x`` has duplicate elements, otherwise False
    """
    return len(set(x)) == len(x)


def triangle_shape(n, fillchar="x", spacechar=" "):
    """Return a string made of ``fillchar`` and ``spacechar``representing a triangle shape of height ``n``.

    For n=0, return ``""``.

    .. testcode::

        from lab1.functions import triangle_shape
        print(triangle_shape(6, fillchar="x", spacechar="_"))

    .. testoutput::

        _____x_____
        ____xxx____
        ___xxxxx___
        __xxxxxxx__
        _xxxxxxxxx_
        xxxxxxxxxxx

    Args:
        n (int): height of the triangle.
        fillchar (str, optional): Defaults to "x".
        spacechar (str, optional): Defaults to " ".

    Returns:
        str: string representation of the triangle.
    """
    width = 2 * n - 1
    return "\n".join(
        (fillchar * (2 * i + 1)).center(width, spacechar) for i in range(n)
    )
>>>>>>> b3c697b0cef6e29f9d6feff78d7cc83350a3b846
