using System;
using System.Collections.Generic;
using System.Linq;

public static class NucleotideCount
{
    private static readonly HashSet<char> NucleotideSymbols = new HashSet<char>("ACGT");

    public static IDictionary<char, int> Count(string sequence)
    {
        var nucleotideCount = NucleotideSymbols.ToDictionary(c => c, c => 0);

        foreach (char nucleotide in sequence)
        {
            CheckNucleotideIsValid(nucleotide);
            nucleotideCount[nucleotide]++;
        }

        return nucleotideCount;
    }

    private static void CheckNucleotideIsValid(char nucleotide)
    {
        if (!NucleotideSymbols.Contains(nucleotide))
        {
            throw new ArgumentException($"{nucleotide} is not a valid nucleotide.");
        }
    }
}
