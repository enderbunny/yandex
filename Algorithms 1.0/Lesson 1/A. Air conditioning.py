t_room, t_cond = map(int, input().split())
# mode = input()

match input():
    case "freeze":
        if t_room > t_cond:
            print(t_cond)
        else:
            print(t_room)
    case "heat":
        if t_room < t_cond:
            print(t_cond)
        else:
            print(t_room)
    case "auto":
        print(t_cond)
    case "fan":
        print(t_room)
