using System.Collections.Generic;

public static class Etl
{
    public static Dictionary<string, int> Transform(Dictionary<int, string[]> old)
    {
        var transformed = new Dictionary<string, int>();
        
        foreach (var (score, letters) in old)
        {
            foreach (var letter in letters)
            {
                transformed.Add(letter.ToLower(), score);
            }
        }

        return transformed;
    }
}
