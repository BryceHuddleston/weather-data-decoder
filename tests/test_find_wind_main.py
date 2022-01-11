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
