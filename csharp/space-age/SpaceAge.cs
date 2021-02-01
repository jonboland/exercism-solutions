using System.Collections.Generic;

public class SpaceAge
{
    private const double EarthYear = 31557600;

    private readonly Dictionary<string, double> orbit = new Dictionary<string, double>
    {
        ["Mercury"] = 0.2408467, ["Venus"] = 0.61519726, ["Mars"] = 1.8808158,
        ["Jupiter"] = 11.862615, ["Saturn"] = 29.447498, ["Uranus"] = 84.016846,
        ["Neptune"] = 164.79132,
    };

    private double earthYears;

    public SpaceAge(int seconds)
    {
        earthYears = seconds / EarthYear;
    }

    public int Seconds { set => earthYears = value / EarthYear; }

    public double OnEarth() => earthYears;

    public double OnMercury() => earthYears / orbit["Mercury"];

    public double OnVenus() => earthYears / orbit["Venus"];

    public double OnMars() => earthYears / orbit["Mars"];

    public double OnJupiter() => earthYears / orbit["Jupiter"];

    public double OnSaturn() => earthYears / orbit["Saturn"];

    public double OnUranus() => earthYears / orbit["Uranus"];

    public double OnNeptune() => earthYears / orbit["Neptune"];
}
