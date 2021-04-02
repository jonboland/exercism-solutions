using System.Linq;

public class Pangram
{
    private const string Alphabet = "abcdefghijklmnopqrstuvwxyz";

    public static bool IsPangram(string input)
    {
        return Alphabet.All(input.ToLower().Contains);
    }
}
