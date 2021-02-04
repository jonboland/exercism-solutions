using System.Collections.Generic;
using System.Linq;

public class HighScores
{
    private List<int> scores;

    public HighScores(List<int> scoreList)
    {
        scores = scoreList;
    }

    public List<int> Scores() => scores;

    public void UpdateScores(List<int> newScores) => scores = newScores;

    public int Latest() => scores.LastOrDefault();

    public int PersonalBest() => scores.DefaultIfEmpty().Max();

    public List<int> PersonalTopThree() =>
        scores.OrderByDescending(s => s).Take(3).ToList();
}
