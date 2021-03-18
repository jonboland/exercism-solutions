using System.Collections.Generic;
using System.Linq;

public class GradeSchool
{
    private readonly SortedList<int, string> register = new SortedList<int, string>();

    public void Add(string student, int grade)
    {
        register.Add(grade, student);
        //register.Sort();
    }

    public IEnumerable<string> Roster()
    {
        return register.Select(r => r.Value);
    }

    public IEnumerable<string> Grade(int grade)
    {
        return register.Where(r => r.Key == grade).Select(r => r.Value);
    }
}
