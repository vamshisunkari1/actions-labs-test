class ArrayIntersection:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def find_intersection(self):
        """Returns the intersection of two sorted arrays without duplicates."""
        intersection = []
        i, j = 0, 0
        
        # Loop through both arrays using two pointers
        while i < len(self.array1) and j < len(self.array2):
            # If the elements are equal, add to the intersection
            if self.array1[i] == self.array2[j]:
                if not intersection or intersection[-1] != self.array1[i]:  # Avoid duplicates
                    intersection.append(self.array1[i])
                i += 1
                j += 1
            # If the element in array1 is smaller, move the pointer of array1
            elif self.array1[i] < self.array2[j]:
                i += 1
            # If the element in array2 is smaller, move the pointer of array2
            else:
                j += 1

        return intersection

# Example Usage
if __name__ == "__main__":
    array1 = [1, 2, 4, 6, 7, 8]
    array2 = [2, 4, 6, 8, 10]

    # Create an object of the ArrayIntersection class
    array_intersection = ArrayIntersection(array1, array2)

    # Find the intersection and print the result
    result = array_intersection.find_intersection()
    print("Intersection of the arrays:", result)
