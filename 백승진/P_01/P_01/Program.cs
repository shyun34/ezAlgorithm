using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace P_01
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] arr = new string[n];

            for (int i = 0; i < n; i++)
            {
                arr[i] = Console.ReadLine();
            }

            //for (int i = 0; i < n; i++)
            //{
            //    Console.WriteLine(arr[i]);
            //}

            List<string> result = new List<string>();

            for(int i = 0; i < n; i++)
            {
                if(arr[i].Contains(" enter"))
                {
                    result.Add(arr[i].Substring(0, arr[i].IndexOf(' ')));
                }
                else
                {
                    result.Remove(arr[i].Substring(0, arr[i].IndexOf(' ')));
                }
            }

            for(int i = 0; i < result.Count; i++)
            {
                Console.WriteLine(result.ElementAt(i));
            }

            Console.ReadKey();
        }
    }
}
