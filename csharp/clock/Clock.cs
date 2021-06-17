using System;

public struct Clock
{
    private const int HoursInDay = 24;
    private const int MinsInHour = 60;

    public Clock(int hours, int minutes)
    {
        double quotient = Math.Floor((double)minutes / MinsInHour);
        Hours = Mod(hours + quotient, HoursInDay);
        Minutes = Mod(minutes, MinsInHour);
    }

    public int Hours { get; }
    public int Minutes { get; }

    public override string ToString() => $"{Hours:00}:{Minutes:00}";

    public Clock Add(int minsToAdd) => new Clock(Hours, Minutes + minsToAdd);

    public Clock Subtract(int minsToSubtract) => Add(-minsToSubtract);

    private static int Mod(double amt, int un) => (((int)amt % un) + un) % un;
}
