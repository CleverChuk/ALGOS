using System;
using System.Collections.Generic;
using System.Linq;


namespace Sort
{
   public static class Program
    {
        static int index = 0;

        static void Main(string[] args)
        {
            //List<int> nums = new List<int>() { 2, 5, 0, 13, 9, 1 ,7,8,89,50};
            Console.WriteLine("Enter sequence to sort: ");
            string num = Console.ReadLine();

            List<int> nums = convertAll(num);
            var sorted = sortFun(nums);

            foreach (var i in sorted)
            {
                Console.WriteLine(i);
            }
            Console.ReadKey();
        }

        public static List<int> sortFun(List<int> sequence)
        {
            
            List<int> sorted = new List<int>(sequence.Count);
            int iteraNum = sequence.Count;

            for (int i = 0; i < iteraNum; i++)
            {
                List<int> data = min(sequence);
                int thismin = data[0];
                int indexx = data[1];
                sorted.Add(thismin);
                sequence[indexx]= int.MaxValue;
              
            }    

            return sorted;
        }

        public static List<int> min(List<int> miniMax)
        {
            int mymin = miniMax[0];
            int newindex = 0;

            foreach (var min in miniMax)
            {
                if (min <= mymin)
                {
                    mymin = min;
                    index = newindex;                    
                }
                newindex++;

            }

            List<int> data = new List < int > { mymin, index };
            return data;
        }


        public static List<int> convertAll(string seq)
        {
            List<int> num = new List<int>();
            string[] seq1;

            seq = seq.Replace(',', ' ');
            seq1 = seq.Split(' ');
            List<string> seq2 = seq1.ToList();
            seq1 = (seq2.FindAll(i => i != "")).ToArray();

            foreach (string str in seq1)
            {   
                num.Add(int.Parse(str));
            }
            return num;
        }

        public static List<int> convertAll(List<int> seq)
        {
            return seq;
        }
    }

}
