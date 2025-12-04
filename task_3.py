points = 0  # Глобалная переменная


class PointsForPlace:

    @staticmethod
    def get_points_for_place(place):
        global points
        if place > 100:
            points = 0
            print('Баллы начисляются только первым 100 участникам')

        elif place < 1:
            points = 0
            print('Спортсмен не может занять нулевое или отрицательное место')

        else:
            points = 101 - place
            return points
        return


class PointsForMeters():

    @staticmethod
    def get_points_for_meters(meters):
        global points
        if meters < 0:
            points = 0
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
            return points
        return


class TotalPoints(PointsForPlace, PointsForMeters):

    @staticmethod
    def get_total_points(meters, place):
        total = PointsForPlace.get_points_for_place(
            place) + PointsForMeters.get_points_for_meters(meters)
        return total


# Не стал менять прекод, но вообще можно не создавать объект, а вызвать как print(имя_класса.статический метод({place}/{meters}))
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
