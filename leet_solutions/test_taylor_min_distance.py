from taylor_min_distance import minTimeToVisitAllPoints


def test_min_time():
    points = [[0, 0], [1, 5], [10, 5]]
    assert minTimeToVisitAllPoints(points) == 14
