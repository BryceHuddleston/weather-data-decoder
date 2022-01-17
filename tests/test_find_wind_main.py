import src.main as main


def test_find_wind_direction_in_observation():
    main.find_wind_in_observation(
        "METAR KGNT 121815Z AUTO 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=")

    assert main.wind_direction == "340"


def test_find_wind_speed_in_observation():
    main.find_wind_in_observation(
        "METAR KJSO 121815Z AUTO 33007G15KT 10SM CLR 18/10 A3019 RMK AO2 T01910098=")

    assert main.wind_speed == "07"


def test_find_gust_speed_in_observation():
    main.find_wind_in_observation(
        "METAR KJSO 121815Z AUTO 33007G15KT 10SM CLR 18/10 A3019 RMK AO2 T01910098=")

    assert main.gust_speed == "15"


def test_find_no_gust_speed_in_observation():
    main.find_wind_in_observation(
        "METAR KJSO 121815Z AUTO 33007KT 10SM CLR 18/10 A3019 RMK AO2 T01910098=")

    assert main.gust_speed == "None"


def test_find_wind_unit_KT_in_observation():
    main.find_wind_in_observation(
        "METAR KJSO 121815Z AUTO 33007KT 10SM CLR 18/10 A3019 RMK AO2 T01910098=")

    assert main.wind_unit == "KT"


def test_find_wind_unit_MPS_in_observation():
    main.find_wind_in_observation(
        "METAR KJSO 121815Z AUTO 33007MPS 10SM CLR 18/10 A3019 RMK AO2 T01910098=")

    assert main.wind_unit == "MPS"


def test_find_wind_direction_VRB_in_observation():
    main.find_wind_in_observation(
        "METAR KNOG 121756Z AUTO VRB05KT 9SM FEW029 26/17 A3014 RMK AO2 SLP187 6//// T02610172 10261 20144 58006 PNO $=")

    assert main.wind_direction == "VRB"


def test_find_wind_direction_for_calm_wind():
    main.find_wind_in_observation(
        "METAR KTOA 121747Z 00000KT 10SM SKC 31/06 A3009=")

    assert main.wind_direction == "000"


def test_find_wind_speed_for_calm_wind():
    main.find_wind_in_observation(
        "METAR KTOA 121747Z 00000KT 10SM SKC 31/06 A3009=")

    assert main.wind_speed == "00"


def test_find_wind_speed_when_over_99():
    main.find_wind_in_observation(
        "METAR KJSO 121815Z AUTO 330107MPS 10SM CLR 18/10 A3019 RMK AO2 T01910098=")

    assert main.wind_speed == "107"


def test_find_gust_speed_when_over_99():
    main.find_wind_in_observation(
        "METAR KJSO 121815Z AUTO 330107G119MPS 10SM CLR 18/10 A3019 RMK AO2 T01910098=")

    assert main.gust_speed == "119"


def test_find_wind_maxes():
    main.find_wind_in_observation(
        "METAR KABC 121755Z AUTO 21016G24KT 180V240 1SM R11/P6000FT -RA BR BKN015 OVC025 06/04 A2990 RMK AO2 PK WND 20032/25 WSHFT 1715 VIS 3/4V1 1/2 VIS 3/4 RWY11 RAB07 CIG 013V017 CIG 017 RWY11 PRESFR SLP125 P0003 60009 T00640036 10066 21012 58033 TSNO $")

    assert main.extreme_clockwise_wind_direction == "240"
    assert main.extreme_counterclockwise_wind_direction == "180"


def test_when_there_is_no_wind_maxes():
    main.find_wind_in_observation(
        "METAR KABC 121755Z AUTO 21016G24KT 1SM R11/P6000FT -RA BR BKN015 OVC025 06/04 A2990 RMK AO2 PK WND 20032/25 WSHFT 1715 VIS 3/4V1 1/2 VIS 3/4 RWY11 RAB07 CIG 013V017 CIG 017 RWY11 PRESFR SLP125 P0003 60009 T00640036 10066 21012 58033 TSNO $")
    assert main.extreme_clockwise_wind_direction == "None"
    assert main.extreme_counterclockwise_wind_direction == "None"
