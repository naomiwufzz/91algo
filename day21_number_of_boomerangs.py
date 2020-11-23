class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:

        def points_distance(point1, point2):
            square_distance = (point1[0]-point2[0]) ** 2 + (point1[1] -point2[0]) ** 2
            return square_distance

        for point in points:
            dic = {}
            for point2 in points:
                if point == point2: continue





points = [[0, 0], [1, 0], [2, 0]]
