using System.Linq;

public static class Bob
{
    public static string Response(string statement)
    {
        if (statement.IsSilent())
        {
            return "Fine. Be that way!";
        }

        if (statement.IsShouted())
        {
            return statement.IsQuestion()
                ? "Calm down, I know what I'm doing!"
                : "Whoa, chill out!";
        }

        return statement.IsQuestion() ? "Sure." : "Whatever.";
    }

    private static bool IsSilent(this string statement) =>
        string.IsNullOrWhiteSpace(statement);

    private static bool IsShouted(this string statement) =>
        statement.Any(char.IsLetter) && !statement.Any(char.IsLower);

    private static bool IsQuestion(this string statement) =>
        statement.TrimEnd().EndsWith('?');
}
