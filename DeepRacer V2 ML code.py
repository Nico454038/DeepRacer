def reward_function(params):
    #start off with 0.001 for the reward
    reward = 0.001

    if params["all_wheels_on_track"]:
        reward += 1
    if abs(params["steering_angle"]) < 5:
        reward += 1
   
    reward += (params["speed"] / 8)
   
    return float(reward)