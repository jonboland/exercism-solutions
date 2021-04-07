using System;
using System.Collections.Generic;
using System.Linq;

public enum Plant
{
    Violets,
    Radishes,
    Clover,
    Grass
}

public class KindergartenGarden
{
    private static readonly string[] Names =
    {
        "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry",
    };

    private readonly Plant[] plantRowOne;
    private readonly Plant[] plantRowTwo;

    public KindergartenGarden(string diagram)
    {
        string[] diagramSplit = diagram.Split('\n');
        plantRowOne = ConvertRow(diagramSplit[0]);
        plantRowTwo = ConvertRow(diagramSplit[1]);
    }

    public IEnumerable<Plant> Plants(string student)
    {
        int leftPlantPosition = Array.IndexOf(Names, student) * 2;
        int rightPlantPosition = leftPlantPosition + 1;

        yield return plantRowOne[leftPlantPosition];
        yield return plantRowOne[rightPlantPosition];
        yield return plantRowTwo[leftPlantPosition];
        yield return plantRowTwo[rightPlantPosition];
    }

    private static Plant[] ConvertRow(string row)
    {
        return row.Select(ConvertLetter).ToArray();
    }

    private static Plant ConvertLetter(char letter)
    {
        return letter switch
        {
            'V' => Plant.Violets,
            'R' => Plant.Radishes,
            'C' => Plant.Clover,
            'G' => Plant.Grass,
            _ => throw new ArgumentException($"Invalid letter: {letter}."),
        };
    }
}
