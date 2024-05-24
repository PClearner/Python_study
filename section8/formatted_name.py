def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)


# test
def city_county(city, county):
    res = f"{city}, {county}"
    return res


a = city_county("santiago", "chile")
print(a)


def make_album(name, album, songs=None):
    if songs == None:
        res = {"singer": name, "album": album}
    else:
        res = {"singer": name, "album": album, "songs": songs}
    return res


a = make_album("star", "buling")
print(a)
b = make_album("jack", "lover", 78)
print(b)
