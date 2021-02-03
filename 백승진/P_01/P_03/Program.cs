using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace P_03
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            int n = int.Parse(str[0]);
            int s = int.Parse(str[1]);

            int k = s - 1;

            List<int> a = new List<int>();
            List<int> result = new List<int>();

            for (int i = 0; i < n; i++)
            {
                a.Add(i + 1);
            }

            while(true)
            {
                result.Add(a.ElementAt(k));
                a.RemoveAt(k);

                if(a.Count <= 0)
                {
                    break;
                }

                k += s - 1;

                while(k >= a.Count)
                {
                    k -= a.Count;
                }
            }

            Console.Write("<");
            for (int i = 0; i < n; i++)
            {
                if(i == n-1)
                {
                    Console.Write($"{result.ElementAt(i)}");
                }
                else
                {
                    Console.Write($"{result.ElementAt(i)}, ");
                }
            }
            Console.Write(">");

            Console.ReadKey();
        }
    }
}
