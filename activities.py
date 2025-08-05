def eat(food, is_healthy):
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"

    return f"I'm eating {food}, {ending}"

def nap(duration):
    hour_label = "hour" if duration == 1 or duration != int(duration) or duration == 0 else "hours"
    if duration < 2:
        return f"I'm feeling refreshed after {duration} {hour_label} of sleep."
    else:
        return f"Ugh I overslept. I didn't mean to nap for {duration} {hour_label}!"
