using System.Text;

public static class RotationalCipher
{
    public static string Rotate(string text, int shiftKey)
    {
        StringBuilder cipherText = new StringBuilder();

        foreach (char c in text)
        {
            if (char.IsLetter(c))
            {
                int start = char.IsLower(c) ? 'a' : 'A';
                int final = (((c + shiftKey) - start) % 26) + start;
                cipherText.Append((char)final);
            }
            else
            {
                cipherText.Append(c);
            }
        }
        return cipherText.ToString();
    }
}
