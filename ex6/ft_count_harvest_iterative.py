def ft_count_harvest_iterative():
    """Count down days to harvest using iteration."""
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print("Day", i)
    print("Harvest time!")
