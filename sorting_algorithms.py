import random

class Sorting:
    def partition_lomuto(A:list, lb:int, hb:int):
        """ 
            This method is responsible for split the sets
        """

        pivot = hb
        i = lb

        for j in range(lb, hb):
            if A[j] <= A[pivot]:  
                A[j], A[i] = A[i], A[j]
                i += 1

        A[i], A[hb] = A[hb], A[i]  
        return i


    def partition_hoare(A:list, lb:int, hb:int):
        """ 
            This method is responsible for split the sets
        """

        pivot = A[lb]
        i = lb - 1
        j = hb + 1
    
        while (True): 
            i += 1
            
            while (A[i] < pivot):
                i += 1
    
            j -= 1
            while (A[j] > pivot):
                j -= 1
    
            if (i >= j):
                return j
    
            A[i], A[j] = A[j], A[i]



    def random_pivot(A:list, lb:int, hb:int):
        """
            This method split set in a ramdomized way.
        """

        random_pivot = random.randrange(lb, hb)
        A[hb], A[random_pivot] = A[random_pivot], A[hb]
        return Sorting.partition_hoare(A, lb, hb)


    def indexed_pivot(A:list, lb:int, hb:int):
        """
            This method split set in a indexed way, using mean value .
        """

        mean_pivot = (lb + hb + ((lb + hb) // 2)) // 3
        A[hb], A[mean_pivot] = A[mean_pivot], A[hb]
        return Sorting.partition_hoare(A, lb, hb)

    def median_pivot(A:list, lb:int, hb:int):
        """
            This method split set in a indexed way, using the median value of each splited set for iteration.
        """
        def get_key(key_values, median: int):
            for key, value in key_values.items():
                if median == value:
                    return key

        key_values = {lb : A[lb], hb : A[hb], hb //2 : A[hb // 2]}
        median = (A[lb], A[hb], A[hb // 2])
        median_sorted = sorted(list(median))
        median_pivot = get_key(key_values, median_sorted[1])
        A[hb], A[median_pivot] = A[median_pivot], A[hb]
        return Sorting.partition_hoare(A, lb, hb)


    def quick_sort(A:list, lb:int, hb:int, pivot_mode:str):
        """
            This method is responsible for call the one of the above split methods recursivily
        """

        if pivot_mode == 'find_pivot':
            if lb < hb:
                pivot = Sorting.partition_hoare(A, lb, hb)
                Sorting.quick_sort(A, lb, pivot - 1, pivot_mode)
                Sorting.quick_sort(A, pivot + 1, hb, pivot_mode)

        if pivot_mode == 'random':
            if lb < hb:
                pivot = Sorting.random_pivot(A, lb, hb)
                Sorting.quick_sort(A, lb, pivot - 1, pivot_mode)
                Sorting.quick_sort(A, pivot + 1, hb, pivot_mode)

        if pivot_mode == 'mean':
            if lb < hb:
                pivot = Sorting.indexed_pivot(A, lb, hb)
                Sorting.quick_sort(A, lb, pivot - 1, pivot_mode)
                Sorting.quick_sort(A, pivot + 1, hb, pivot_mode)

        if pivot_mode == 'median':
            if lb < hb:
                pivot = Sorting.median_pivot(A, lb, hb)
                Sorting.quick_sort(A, lb, pivot - 1, pivot_mode)
                Sorting.quick_sort(A, pivot + 1, hb, pivot_mode)

