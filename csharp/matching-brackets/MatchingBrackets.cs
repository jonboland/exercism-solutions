using System.Collections.Generic;
using System.Linq;

public static class MatchingBrackets
{
    private const string OpeningBrackets = "{[(";
    private const string ClosingBrackets = "}])";

    public static bool IsPaired(string input)
    {
        Stack<char> unpairedBrackets = new();

        foreach (char character in input)
        {
            if (OpeningBrackets.Contains(character))
            {
                unpairedBrackets.Push(character);
            }
            else if (ClosingBracketsContains(character, out int closingBracketIndex))
            {
                if (BracketsMatch(closingBracketIndex, unpairedBrackets))
                {
                    unpairedBrackets.Pop();
                }
                else
                {
                    return false;
                }
            }
        }

        return !unpairedBrackets.Any();
    }

    private static bool ClosingBracketsContains(char character, out int closingBracketIndex)
    {
        closingBracketIndex = ClosingBrackets.IndexOf(character);

        return closingBracketIndex != -1;
    }

    private static bool BracketsMatch(int closingBracketIndex, Stack<char> unpairedBrackets)
    {
        char openingBracket = OpeningBrackets[closingBracketIndex];

        return unpairedBrackets.TryPeek(out char stackTop) && stackTop == openingBracket;
    }
}
