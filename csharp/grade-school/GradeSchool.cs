using System.Collections.Generic;
using System.Linq;

public class GradeSchool
{
    private List<(int Year, string Name)> register = new List<(int, string)>();

    public void Add(string student, int grade)
    {
        register.Add((grade, student));
        register.Sort();
    }

    public IEnumerable<string> Roster()
    {
        return register.Select(r => r.Name);
    }

    public IEnumerable<string> Grade(int grade)
    {
        return register.Where(r => r.Year == grade).Select(r => r.Name);
    }
}
