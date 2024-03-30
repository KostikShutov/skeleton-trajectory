from components.coordinate.Coordinate import Coordinate


class CoordinateTransformer:
    def separateToXYLists(self, coordinates: list[Coordinate]) -> tuple[list[float], list[float]]:
        x: list[float] = []
        y: list[float] = []

        for coordinate in coordinates:
            x.append(coordinate.x)
            y.append(coordinate.y)

        return x, y

    def splitInfoFragments(self, coordinates: list[Coordinate]) -> list[list[Coordinate]]:
        fragments: list[list[Coordinate]] = []

        for i in range(len(coordinates)):
            try:
                fragments.append([
                    coordinates[i],
                    coordinates[i + 1],
                    coordinates[i + 2],
                ])
            except IndexError:
                continue

        return fragments

    def addFictionalCoordinates(self, coordinates: list[Coordinate], count: int) -> list[Coordinate]:
        if count <= 0:
            return []

        try:
            last: Coordinate = coordinates[-1]
            prev: Coordinate = coordinates[-2]
        except IndexError:
            return []

        dx = last.x - prev.x
        dy = last.y - prev.y

        for _ in range(count):
            coordinates.append(Coordinate(
                x=coordinates[-1].x + dx,
                y=coordinates[-1].y + dy,
            ))

        return coordinates
