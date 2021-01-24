public static class ResistorColor
{
    private static readonly string[] resistorColors = { "black", "brown", "red", "orange",
        "yellow", "green", "blue", "violet", "grey", "white" };
    
    public static int ColorCode(string color) => System.Array.IndexOf(resistorColors, color);
    
    public static string[] Colors() => resistorColors;
}