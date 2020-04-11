class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        dist = 0
        for (x0, y0), (x1, y1) in zip(points, points[1:]):
            dist += max(abs(x0 - x1), abs(y0 - y1))

        return dist
