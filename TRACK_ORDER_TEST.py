#Вахтина Софья 8-я когорта - диплом

from SENDER import create_order, get_order
def test_get_order():

    track = create_order()
    assert track is not None
    status_code, _ = get_order(track)
    assert status_code == 200