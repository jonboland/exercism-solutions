using System.Collections.Generic;
using System.Linq;

public static class Isogram
{
    public static bool IsIsogram(string word)
    {
        var set = new HashSet<char>();

        return word.ToLower().Where(char.IsLetter).All(set.Add);
    }
}
