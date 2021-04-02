using System;
using System.Collections.Generic;
namespace Tubes2
{
    public class Program
    {
        static void Main()
        {
            try
            { 
                Graph g;
                Console.Write("Input file: ");
                string input = Console.ReadLine();
                g = Graph.GraphFromFile(input);

                //g.PrintToConsole();
                Console.Write("Start Node: ");
                string s = Console.ReadLine();
                Console.Write("End Node: ");
                string e = Console.ReadLine();
                Vertex start = g.findVertex(s);
                Vertex end = g.findVertex(e);
                Console.WriteLine("Explore BFS: ");
                g.explore_friend(start, end, "BFS");
                Console.WriteLine("Explore DFS: ");
                g.explore_friend(start, end, "DFS");

                string result = g.FriendRecommendation(g.findVertex("A"));
                Console.WriteLine(result);

            } catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}