import retro

env = retro.make(game="StreetFighterIISpecialChampionEdition-Genesis")
state = env.reset()

done = False
for game in range(1):
    while not done:
        if done:
            state = env.reset()
        env.render()
        state, reward, done, truncated, info = env.step(env.action_space.sample())
