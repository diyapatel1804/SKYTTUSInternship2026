using System;
using System.Collections.Generic;
using System.Linq;

class Student
{
    // Encapsulation (Properties)
    public int StudentId { get; set; }
    public string Name { get; set; }
    public string Department { get; set; }
    public int Year { get; set; }
    public int Marks { get; set; }

    // Constructor
    public Student(int id, string name, string dept, int year, int marks)
    {
        StudentId = id;
        Name = name;
        Department = dept;
        Year = year;
        Marks = marks;
    }

    // Method to display student details
    public void Display()
    {
        Console.WriteLine($"{StudentId} | {Name} | {Department} | Year: {Year} | Marks: {Marks}");
    }
}

class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>();

        Console.Write("Enter number of students: ");
        int count = int.Parse(Console.ReadLine());

        for (int i = 0; i < count; i++)
        {
            Console.WriteLine($"\nEnter details for Student {i + 1}");

            Console.Write("ID: ");
            int id = int.Parse(Console.ReadLine());

            Console.Write("Name: ");
            string name = Console.ReadLine();

            Console.Write("Department: ");
            string dept = Console.ReadLine();

            Console.Write("Year: ");
            int year = int.Parse(Console.ReadLine());

            Console.Write("Marks: ");
            int marks = int.Parse(Console.ReadLine());

            students.Add(new Student(id, name, dept, year, marks));
        }

        // 1. Display all students
        Console.WriteLine("\n--- All Students ---");
        foreach (var s in students)
        {
            s.Display();
        }

        // 2. Students with marks > 75
        Console.WriteLine("\n--- Students with Marks > 75 ---");
        var highMarks = students.Where(s => s.Marks > 75);
        foreach (var s in highMarks)
        {
            s.Display();
        }

        // 3. Sort by marks
        Console.WriteLine("\n--- Sorted by Marks (Descending) ---");
        var sorted = students.OrderByDescending(s => s.Marks);
        foreach (var s in sorted)
        {
            s.Display();
        }

        // 4. Top 3 scorers
        Console.WriteLine("\n--- Top 3 Scorers ---");
        var top3 = students.OrderByDescending(s => s.Marks).Take(3);
        foreach (var s in top3)
        {
            s.Display();
        }
    }
}