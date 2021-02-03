using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace P_04
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

            Stack<int> s = new Stack<int>();

            for (int i = 0; i < n; i++)
            {
                if(arr[i].Contains("push"))
                {
                    s.Push(int.Parse(arr[i].Substring(arr[i].IndexOf(' ')+1)));
                }
                else if(arr[i].Contains("pop"))
                {
                    if(s.Count <= 0)
                    {
                        Console.WriteLine(-1);
                    }
                    else
                    {
                        Console.WriteLine(s.Pop());
                    }
                }
                else if(arr[i].Contains("size"))
                {
                    Console.WriteLine(s.Count);
                }
                else if(arr[i].Contains("empty"))
                {
                    if(s.Count <= 0)
                    {
                        Console.WriteLine(1);
                    }
                    else
                    {
                        Console.WriteLine(0);
                    }
                }
                else if(arr[i].Contains("top"))
                {
                    Console.WriteLine(s.Peek());
                }
            }

            Console.ReadKey();
        }
    }
}
