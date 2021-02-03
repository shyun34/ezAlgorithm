using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace P_05
{
    class Program
    {
        static void Main(string[] args)
        {
            string v = Console.ReadLine();

            Stack<char> s = new Stack<char>();

            bool a = true;

            int result = 0;

            for (int i = 0; i < v.Length; i++)
            {
                if(i == 0)
                {
                    s.Push(v.ElementAt(i));
                }
                else
                {
                    if (s.Count > 0)
                    {
                        if (s.Peek().Equals('('))
                        {
                            if (v.ElementAt(i).Equals(')'))
                            {
                                s.Pop();
                            }
                            else
                            {
                                s.Push(v.ElementAt(i));
                            }
                        }
                        else if (s.Peek().Equals('['))
                        {
                            if (v.ElementAt(i).Equals(']'))
                            {
                                s.Pop();
                            }
                            else
                            {
                                s.Push(v.ElementAt(i));
                            }
                        }
                    }
                    else
                    {
                        s.Push(v.ElementAt(i));
                    }
                }
            }

            if (s.Count > 0)
            {
                a = false;
            }
            else
            {
                a = true;
            }

            if(a)
            {
                for (int i = 0; i < v.Length; i++)
                {
                    if (i == 0)
                    {
                        s.Push(v.ElementAt(i));
                    }
                    else
                    {
                        if (s.Count > 0)
                        {
                            if (s.Peek().Equals('('))
                            {
                                if (v.ElementAt(i).Equals(')'))
                                {
                                    s.Pop();
                                    s.Push('2');
                                }
                                else
                                {
                                    s.Push(v.ElementAt(i));
                                }
                            }
                            else if (s.Peek().Equals('['))
                            {
                                if (v.ElementAt(i).Equals(']'))
                                {
                                    s.Pop();
                                    s.Push('3');
                                }
                                else
                                {
                                    s.Push(v.ElementAt(i));
                                }
                            }
                            else
                            {
                                s.Push(v.ElementAt(i));
                            }
                        }
                        else
                        {
                            s.Push(v.ElementAt(i));
                        }
                    }
                }

                int t = 1;
                int num = 0;

                while(s.Count <= 0)
                {
                    if (s.Peek().Equals(')'))
                    {
                        t *= 2;
                        s.Pop();
                    }
                    else if (s.Peek().Equals('('))
                    {
                        result = num * t;
                        t = 1;
                        num = 0;
                        s.Pop();
                    }
                    else if (s.Peek().Equals(']'))
                    {
                        t *= 3;
                        s.Pop();
                    }
                    else if (s.Peek().Equals('['))
                    {
                        result += num * t;
                        t = 1;
                        num = 0;
                        s.Pop();
                    }
                    else
                    {
                        num += int.Parse(s.Pop().ToString());
                    }
                }
            }

            Console.WriteLine(result);

            Console.ReadKey();
        }
    }
}
