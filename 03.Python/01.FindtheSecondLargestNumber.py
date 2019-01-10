if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    unique_array = list(set(arr))
    unique_array.sort(reverse=True)
    print (unique_array[1])