import math

def main():
    for i in range(0, DefineConstants.MAX):
        Globals.a[i] = math.fmod(rand(), 100)


    t1 = clock_t()
    t2 = clock_t()

    t1 = clock()
    threads = [pthread_t() for _ in range(DefineConstants.THREAD_MAX)]

    for i in range(0, DefineConstants.THREAD_MAX):
        pthread_create(threads[i], None, merge_sort, None)

    for i in range(0, 4):
        pthread_join(threads[i], None)

#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
    Globals.merge(0, (DefineConstants.MAX / 2 - 1) / 2, DefineConstants.MAX / 2 - 1)
#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
    Globals.merge(DefineConstants.MAX / 2, DefineConstants.MAX/2 + (DefineConstants.MAX-1-DefineConstants.MAX/2)/2, DefineConstants.MAX - 1)
#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
    Globals.merge(0, (DefineConstants.MAX - 1)/2, DefineConstants.MAX - 1)

    t2 = clock()

    print("Sorted array: ", end = '')
    for i in range(0, DefineConstants.MAX):
        print(Globals.a[i], end = '')
        print(" ", end = '')

    print("Time taken: ", end = '')
    print((t2 - t1) / float(CLOCKS_PER_SEC), end = '')
    print("\n", end = '')


class Globals:
    #C++ TO PYTHON CONVERTER WARNING: The following #include directive was ignored:
    ##include <pthread.h>

    a = [0 for _ in range(DefineConstants.MAX)]
    part = 0

    @staticmethod
    def merge(low, mid, high):
        left = [0 for _ in range(mid - low + 1)]
        right = [0 for _ in range(high - mid)]

        n1 = mid - low + 1
        n2 = high - mid
        i = None
        j = None

        for i in range(0, n1):
            left[i] = Globals.a[i + low]

        for i in range(0, n2):
            right[i] = Globals.a[i + mid + 1]

        k = low
        i = j = 0

        while i < n1 and j < n2:
            if left[i] <= right[j]:
#C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: a[k++] = left[i++];
                Globals.a[k] = left[i]
                i += 1
                k += 1
            else:
#C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: a[k++] = right[j++];
                Globals.a[k] = right[j]
                j += 1
                k += 1

        while i < n1:
#C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: a[k++] = left[i++];
            Globals.a[k] = left[i]
            i += 1
            k += 1

        while j < n2:
#C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: a[k++] = right[j++];
            Globals.a[k] = right[j]
            j += 1
            k += 1

    @staticmethod
    def merge_sort(low, high):
        mid = low + math.trunc((high - low) / float(2))
        if low < high:

            Globals.merge_sort(low, mid)

            Globals.merge_sort(mid + 1, high)

            Globals.merge(low, mid, high)

    @staticmethod
    def merge_sort(arg):

#C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: int thread_part = part++;
        thread_part = Globals.part
        Globals.part += 1

#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        low = thread_part * (DefineConstants.MAX / 4)
#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        high = (thread_part + 1) * (DefineConstants.MAX / 4) - 1

        mid = low + math.trunc((high - low) / float(2))
        if low < high:
            Globals.merge_sort(low, mid)
            Globals.merge_sort(mid + 1, high)
            Globals.merge(low, mid, high)

class DefineConstants:
    MAX = 20
    THREAD_MAX = 4

if __name__ == "__main__":
    main()
