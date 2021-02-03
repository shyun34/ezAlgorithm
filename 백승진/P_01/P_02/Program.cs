using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace P_02
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<int> arr = new List<int>();

            for (int i = 0; i < n; i++)
            {
                arr.Add(int.Parse(Console.ReadLine()));
            }

            arr.Sort();

            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(arr.ElementAt(i));
            }

            Console.ReadKey();
        }
    }
}
