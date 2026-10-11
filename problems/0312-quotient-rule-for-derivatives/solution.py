import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g=np.array(g_coeffs)
    h=np.array(h_coeffs)

    g_val=np.polyval(g,x)
    h_val=np.polyval(h,x)

    dg=np.polyval(np.polyder(g),x)
    dh=np.polyval(np.polyder(h),x)
    
    val=(dg*h_val-g_val*dh)/h_val**2
    return val
    pass