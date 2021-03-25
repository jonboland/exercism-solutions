public static class BinarySearch
{
    public static int Find(int[] input, int value)
    {
        var low = 0;
        var high = input.Length - 1;

        while (low <= high)
        {
            var middle = (low + high) / 2;
            var check = input[middle];

            if (check == value)
            {
                return middle;
            }

            if (check < value)
            {
                low = middle + 1;
            }
            else
            {
                high = middle - 1;
            }
        }

        return -1;
    }
}
