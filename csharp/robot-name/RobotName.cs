using System;
using System.Collections.Generic;

public class Robot
{
    private const string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private const int MaximumNumberOfRobots = 675_000;
    private static readonly Random Rand = new Random();
    private static HashSet<string> names = new HashSet<string>();

    public Robot()
    {
        Reset();
    }

    public string Name { get; private set; }

    public void Reset()
    {
        LimitNumberOfRobotNames();
        do
        {
            GenerateRandomRobotName();
        }
        while (!names.Add(Name));
    }

    private void LimitNumberOfRobotNames()
    {
        if (names.Count > MaximumNumberOfRobots)
        {
            throw new InvalidOperationException(
                "Factory settings could not be applied "
                + "because it wasn't possible to generate "
                + "a new robot name. Please contact the "
                + "manufacturer for assistance.");
        }
    }

    private void GenerateRandomRobotName()
    {
        Name = Alphabet[Rand.Next(26)].ToString();
        Name += Alphabet[Rand.Next(26)];
        Name += Rand.Next(1000).ToString("D3");
    }
}
