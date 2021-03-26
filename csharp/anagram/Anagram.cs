using System;
using System.Linq;

public class Anagram
{
    private readonly string wordUpper;
    private readonly string sortedWordUpper;

    public Anagram(string baseWord)
    {
        wordUpper = baseWord.ToUpper();
        sortedWordUpper = SortString(baseWord);
    }

    public string[] FindAnagrams(string[] potentialMatches)
    {
        return potentialMatches
            .Where(p => p.ToUpper() != wordUpper)
            .Where(p => SortString(p) == sortedWordUpper)
            .ToArray();
    }

    private string SortString(string word)
    {
        char[] chars = word.ToUpper().ToCharArray();
        Array.Sort(chars);

        return new string(chars);
    }
}
