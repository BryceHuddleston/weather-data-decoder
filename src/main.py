import re

wind_direction = None
wind_speed = None
gust_speed = None
wind_unit = None


def find_icao_in_observation(observation):
    if re.match("(METAR|SPECI|LWIS)?( COR)? ?([A-Z]{4} )", observation):
        x = re.match("(METAR|SPECI|LWIS)?( COR)? ?([A-Z]{4} )", observation)
        icao = x.group(3).strip()
    else:
        icao = "None"

    return icao


def find_modifier_in_observation(observation):
    if " AUTO " in observation:
        modifier = "AUTO"
    elif " COR " in observation:
        modifier = "COR"
    else:
        modifier = "None"

    return modifier


def find_wind_in_observation(observation):
    global wind_direction
    global wind_speed
    global gust_speed
    global wind_unit

    x = re.match(
        "(METAR|SPECI|LWIS)?( COR)? ?([A-Z]{4} )(\d+)Z (AUTO )?(.+)(KT|MPS)", observation)
    wind_section = x.group(6)

    wind_direction = wind_section[:3]
    wind_unit = x.group(7)

    if "G" in wind_section:
        speeds = wind_section.split("G")
        wind_speed = speeds[0][3:]
        gust_speed = speeds[1]
    else:
        wind_speed = wind_section[3:]
        gust_speed = "None"
