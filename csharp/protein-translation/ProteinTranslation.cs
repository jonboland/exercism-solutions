using System;
using System.Collections.Generic;
using System.Linq;

public static class ProteinTranslation
{
    public static string[] Proteins(string strand)
    {
        return Chunks(strand)
            .Select(Translate)
            .TakeWhile(protein => protein != "STOP")
            .ToArray();
    }

    private static IEnumerable<string> Chunks(string strand)
    {
        if (strand.Length is var length && length % 3 != 0)
        {
            throw new ArgumentException($"Invalid strand length: {length}.");
        }

        for (int i = 0; i < length; i += 3)
        {
            yield return strand.Substring(i, 3);
        }
    }

    private static string Translate(string codon)
    {
        return codon switch
        {
            "AUG" => "Methionine",
            "UUC" or "UUU" => "Phenylalanine",
            "UUA" or "UUG" => "Leucine",
            "UCU" or "UCC" or "UCA" or "UCG" => "Serine",
            "UAU" or "UAC" => "Tyrosine",
            "UGU" or "UGC" => "Cysteine",
            "UGG" => "Tryptophan",
            "UAA" or "UAG" or "UGA" => "STOP",
            _ => throw new ArgumentException($"Invalid codon: {codon}."),
        };
    }
}
