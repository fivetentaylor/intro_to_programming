def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_distance = 0
        for i in range(len(points) - 1):
            starting_point = points[i]
            end_point = points[i + 1]
            
            xs = starting_point[0]
            ys = starting_point[1]
            xz = end_point[0]
            yz = end_point[1]
            distance = max([abs(xs - xz), abs(ys - yz)])
            total_distance = total_distance + distance
        
        return total_distance