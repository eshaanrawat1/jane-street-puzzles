# dice.py

front_states = {}
back_states = {}
left_states = {}
right_states = {}

def generate_seeds():
    seeds = []

    faces = [1,2,3,4,5,6]
    for top in faces:
        bot = 7 - top

        for front in faces:
            if front != top and front != bot:
                back = 7 - front
                left, right = [side for side in faces if side not in [top, bot, front, back]]
                seeds.append((top, bot, front, back, left, right))

    return seeds

        
def vert_roll(top, bot, front, back):
    res = []
    for _ in range(4):
        top, front, bot, back = back, top, front, bot
        res.append(str(top) + str(front))
    return res


def horiz_roll(top, bot, front, back, left, right):
    res = []
    for _ in range(4):
        top, bot, front, back, left, right = left, right, front, back, bot, top
        res.append(str(top) + str(front))
    return res


def compute():
    seeds = generate_seeds()

    for top, bot, front, back, _, _ in seeds:
        vk = vert_roll(top, bot, front, back)
        for i in range(len(vk)):
            front_states[vk[i]] = vk[i-1]
            back_states[vk[i-1]] = vk[i]

    for top, bot, front, back, left, right in seeds:
        hk = horiz_roll(top, bot, front, back, left, right)
        for i in range(len(hk)):
            left_states[hk[i]] = hk[i-1]
            right_states[hk[i-1]] = hk[i]

    return left_states, right_states, front_states, back_states