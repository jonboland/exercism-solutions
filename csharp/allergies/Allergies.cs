using System;
using System.Linq;

[Flags]
public enum Allergen : byte
{
    Eggs = 0b_0000_0001,
    Peanuts = 0b_0000_0010,
    Shellfish = 0b_0000_0100,
    Strawberries = 0b_0000_1000,
    Tomatoes = 0b_0001_0000,
    Chocolate = 0b_0010_0000,
    Pollen = 0b_0100_0000,
    Cats = 0b_1000_0000,
}

public class Allergies
{
    public Allergies(int mask) => Mask = mask;

    public int Mask { get; set; }

    public bool IsAllergicTo(Allergen allergen)
    {
        return (Mask & (byte)allergen) != 0;
    }

    public Allergen[] List()
    {
        return (from Allergen allergen
                in Enum.GetValues(typeof(Allergen))
                where IsAllergicTo(allergen)
                select allergen).ToArray();
    }
}
