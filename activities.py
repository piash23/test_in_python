def eat(food, is_healthy=True):
    """
    Returns a message about eating food based on whether it's healthy or not.
    
    Args:
        food (str): The name of the food being eaten
        is_healthy (bool): Whether the food is healthy or not
        
    Returns:
        str: A message about eating the food
    """
    if is_healthy:
        return f"I'm eating {food}, because my body is a temple"
    else:
        return f"I'm eating {food}, because YOLO!"


def nap(hours):
    """
    Returns a message about napping based on the duration.
    
    Args:
        hours (int): Number of hours to nap
        
    Returns:
        str: A message about the nap experience
    """
    if hours < 2:
        return f"I'm feeling refreshed after {hours} hour of sleep."
    else:
        return f"Ugh I overslept. I didn't mean to nap for {hours} hours!"