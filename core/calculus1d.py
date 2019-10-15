import numpy as np

def integral(func, start, end, precise, y_method):
    “”“
    Desc: Calculate integral of 1 dimensional function
    Parameters:
        func: A str representing f(x)
        start: The start point of x to calculate integral
        end: The end point of x to calculate integral
        precise: A int indicting the precision of calculation
        y_method: A str, left or right, which decide which side of function value we use
    Return: The value of integral
    ”“”
    if end < start:
        raise Exception("start must smaller than end")

    # (1) Decoding func and create
    interval = np.abs(end - start)
    delta = 10**(-precise)
    number = int(interval/delta)
    x = np.linspace(start, end, number).reshape(number, 1)
    y = eval(func)

    # (2) Calculating integral
    if y_method == 'left':
        result = np.array([[delta] * (number - 1)]) @ y[:number-1, :]
    elif y_method == 'right':
        result = np.array([[delta] * (number - 1)]) @ y[1:, :]

    result = result[0, 0]
    return result

def derivative(func, point, precise):
    """
    Parameters:
       func: func: A str representing f(x)
       point: A number indicating the point to solve derivative
       precise: A number indicating the precision of calculation
    """
    delta = 10**(-precise)
    x1 = point - delta
    x2 = point + delta
    x = np.array([x1, x2])
    y = eval(func)
    result = (y[1] - y[0])/(x[1] - x[0])

    return result

if __name__ == '__main__':
    f = '2*x + x**2'
    deriv = derivative(func=f, point=2, precise=5)
    integ = integral(func=f, start=0, end=5, precise=5, y_method='left')
