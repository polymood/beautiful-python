from typing import List, Tuple

class Statistics:
    """A class to perform statistical computations on a list of numbers."""

    def __init__(self, data: List[float]):
        self.data = data

    def mean(self) -> float:
        """Calculate the mean of the data.

        Returns:
            float: The mean of the data.
        """
        if not self.data:
            raise ValueError("The data list is empty.")
        return sum(self.data) / len(self.data)

    def median(self) -> float:
        """Calculate the median of the data.

        Returns:
            float: The median of the data.
        """
        if not self.data:
            raise ValueError("The data list is empty.")
        
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def variance(self) -> float:
        """Calculate the variance of the data.

        Returns:
            float: The variance of the data.
        """
        if not self.data:
            raise ValueError("The data list is empty.")
        
        mean_value = self.mean()
        return sum((x - mean_value) ** 2 for x in self.data) / len(self.data)

    def standard_deviation(self) -> float:
        """Calculate the standard deviation of the data.

        Returns:
            float: The standard deviation of the data.
        """
        return self.variance() ** 0.5

def main() -> None:
    """Main function to demonstrate the use of the Statistics class."""
    data = [10.5, 14.2, 18.6, 20.1, 22.5]
    stats = Statistics(data)

    print(f"Data: {data}")
    print(f"Mean: {stats.mean()}")
    print(f"Median: {stats.median()}")
    print(f"Variance: {stats.variance()}")
    print(f"Standard Deviation: {stats.standard_deviation()}")

if __name__ == "__main__":
    main()
