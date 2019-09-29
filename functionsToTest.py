def eat(food, is_healthy):
    ending = "it's not healthy"
    if is_healthy:
        ending = "my body is a temple"

    return f"I'm eating {food} because {ending}"


def nap(num_of_hours):
    if num_of_hours < 2:
        return f"Might need to snooze, I only slept for {num_of_hours} hour, don't feel refreshed!"
    return f"Feel refreshed because I slept for {num_of_hours} hours!"
