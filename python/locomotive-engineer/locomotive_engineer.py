"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    [a, b, c, *tail] = each_wagons_id
    return [c, *missing_wagons, *tail, a, b]


def add_missing_stops(from_to, **stops):
    return {**from_to, "stops": list(stops.values())}


def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    return [list(item) for key, item in enumerate(list(zip(*wagons_rows)))]
