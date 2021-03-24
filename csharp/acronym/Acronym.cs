using System.Linq;
using System.Text.RegularExpressions;

public static class Acronym
{
    public static string Abbreviate(string phrase)
    {
        MatchCollection result = Regex.Matches(phrase.ToUpper(), "[A-Z']+");
        
        return string.Join("", result.Select(m => m.Value[0]));
    }
}
