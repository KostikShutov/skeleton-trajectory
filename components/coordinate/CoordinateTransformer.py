from components.coordinate.Coordinate import Coordinate


class CoordinateTransformer:
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

    def addFictionalCoordinate(self, coordinates: list[Coordinate]) -> list[Coordinate]:
        try:
            last: Coordinate = coordinates[-1]
            prev: Coordinate = coordinates[-2]
        except IndexError:
            return []

        coordinates.append(Coordinate(
            x=2 * last.x - prev.x,
            y=2 * last.y - prev.y,
        ))

        return coordinates
