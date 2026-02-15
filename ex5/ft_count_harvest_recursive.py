def ft_count_harvest_recursive():
    """Count down days to harvest using recursion."""
    days = int(input("Days until harvest: "))

    def count_helper(current, total):
        if current <= total:
            print("Day", current)
            count_helper(current + 1, total)
    count_helper(1, days)
    print("Harvest time!")
