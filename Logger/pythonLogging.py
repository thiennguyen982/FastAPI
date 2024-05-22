import logging
import math as m

#CREATE AND CONFIGURE THE LOGGER
def create_logger(filename : str):
    LOG_FORMAT = "%(levelname)s - %(asctime)s - %(message)s"
    logging.basicConfig(filename=filename,
                        level=logging.DEBUG,
                        format=LOG_FORMAT,
                        filemode="a")
    logger = logging.getLogger()
    return logger

logger = create_logger("logging.log")

def quadratic_formula(a, b, c):
    """_summary_

    Args:
        a (_type_): ^2 number 
        b (_type_): ^1 number
        c (_type_): residue
    """
    
    logger.info(f"Quadratic Formula: {a}*x^2 + {b}*x + c")
    
    #Compute discriminant
    logger.debug("Compute Discriminant")
    delta = m.pow(b, 2) - 4 * a * c
    
    if delta < 0:
        return "No roots"
    
    #Compute roots
    logger.debug("Root computation")
    
    root1 = (-b + m.sqrt(delta)) / (2 * a)
    root2 = (-b - m.sqrt(delta)) / (2 * a)
    
    return (root1, root2)

print(quadratic_formula(1, -2, -8))