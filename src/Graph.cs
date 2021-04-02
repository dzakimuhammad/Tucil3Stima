using System;
using System.Collections.Generic;

namespace Tubes2
{
    public class Graph
    {

        public List<Vertex> AdjacencyList
        {
            get;
            set;
        }

        // Constructor
        public Graph()
        {
            AdjacencyList = new List<Vertex>();
        }

        // Construct Graph from a txt file
        public static Graph GraphFromFile(string filename)
        {
            Graph g = new Graph();

            string[] lines = System.IO.File.ReadAllLines(filename);

            for (int i = 1; i < lines.Length; i++)
            {
                string[] vs = lines[i].Split(' ');
                if (g.IsNewVertex(vs[0]))
                {
                    g.AddVertex(vs[0]);
                }
                if (g.IsNewVertex(vs[1]))
                {
                    g.AddVertex(vs[1]);
                }
                Vertex v0 = new Vertex(vs[0]);
                Vertex v1 = new Vertex(vs[1]);
                g.AddEdge(v0, v1);
            }

            foreach(Vertex v in g.AdjacencyList)
            {
                v.Edges.Sort((a, b) => a.Name.CompareTo(b.Name));
            }

            return g;
        }

        // I.S. = newVertex belum terdapat dalam graf.
        // F.S. = newVertex ditambahkan dalam graf.
        public void AddVertex(string newVertex)
        {
            AdjacencyList.Add(new Vertex(newVertex));
        }

        // Mengembalikan simpul bernama ver, jika tidak ada mengembalikan simpul bernama "null"
        public Vertex findVertex(string ver)
        {
            foreach (Vertex v in AdjacencyList)
            {
                if (v.Name == ver)
                {
                    return v;
                }
            }
            Vertex v1 = new Vertex("null");
            return v1;
        }

        public void AddEdge(Vertex v1, Vertex v2)
        {
            AdjacencyList.Find(v => v.Name == v1.Name).Edges.Add(v2);
            AdjacencyList.Find(v => v.Name == v2.Name).Edges.Add(v1);
        }

        public void RemoveEdge(Vertex v1, Vertex v2)
        {
            AdjacencyList.Find(v => v.Name == v1.Name).Edges.Remove(v2);
            AdjacencyList.Find(v => v.Name == v2.Name).Edges.Remove(v1);
        }

        public bool IsNewVertex(string newVertex)
        {
            return AdjacencyList.Find(v => v.Name == newVertex) == null;
        }

        public bool IsConnected(Vertex v1, Vertex v2)
        {
            return AdjacencyList.Find(v => v.Name == v1.Name).Edges.Contains(v2) && AdjacencyList.Find(v => v.Name == v2.Name).Edges.Contains(v1);
        }

        public void PrintToConsole()
        {
            foreach (Vertex v in AdjacencyList)
            {
                Console.Write("Vertex " + v.Name + " -> ");
                v.Edges.ForEach(i => Console.Write("{0} ", i.Name));
                Console.WriteLine();
            }
        }

        // Mencari jalur pada graf dengan BFS
        public List<string> bfs(Vertex s, Vertex e, Dictionary<string, bool> dikunjungi, Dictionary<string, string> prev )
        {
            Queue<Vertex> q = new Queue<Vertex>();

            q.Enqueue(s);
            dikunjungi[s.Name] = true;

            while (q.Count > 0)
            {
                Vertex node = q.Dequeue();
                Vertex n = findVertex(node.Name);
                if (n.Name == e.Name)
                {
                    break;
                }
                foreach (Vertex next in n.Edges)
                {
                    if (dikunjungi[next.Name] == false)
                    {
                        dikunjungi[next.Name] = true;
                        prev[next.Name] = n.Name;
                        q.Enqueue(next);
                    }
                }
            }

            return path(s, e, prev);
        }

        // Mencari jalur pada graf dengan DFS
        public List<string> dfs(Vertex s, Vertex e, Dictionary<string, bool> dikunjungi, Dictionary<string, string> prev)
        {
            dikunjungi[s.Name] = true;

            Vertex n = findVertex(s.Name);
            if(n.Name != e.Name){
                foreach(Vertex next in n.Edges){
                    if(dikunjungi[next.Name] == false){
                        prev[next.Name] = n.Name;
                        dfs(next, e, dikunjungi, prev);
                    }
                }
            }

            return path(s, e, prev);
        }

        // Mencari jalur dari simpul s ke simpul e
        public List<string> path(Vertex s, Vertex e, Dictionary<string, string> prev)
        {
            List<string> jalur = new List<string>();
            string i = e.Name;
            while (i != null)
            {
                jalur.Add(i);
                i = prev[i];
            }
            jalur.Reverse();

            if (jalur[0] == s.Name)
            {
                return jalur;
            }
            List<string> list1 = new List<string>() { };
            return list1;
        }

        // Fitur Explore Friends
        public Tuple<List<string>, string> explore_friend(Vertex s, Vertex e, string metode)
        {
            Dictionary<string, bool> dikunjungi = new Dictionary<string, bool>();
            Dictionary<string, string> prev = new Dictionary<string, string>();
            List<string> path;

            //  Menandai dikunjungi dengan false
            foreach (Vertex node in AdjacencyList)
            {
                dikunjungi[node.Name] = false;
            }

            foreach (Vertex node in AdjacencyList)
            {
                prev[node.Name] = null;
            }

            //  Mengambil jalur sesuai dengan inpu algoritma
            if (String.Compare(metode.ToUpper(), "BFS") == 0)
            {
                path = bfs(s, e, dikunjungi, prev);
            }

            else
            {
                if (String.Compare(metode.ToUpper(), "DFS") == 0)
                {
                    path = dfs(s, e, dikunjungi, prev);
                }
                else
                {
                    return new Tuple<List<string>, string>(new List<string>(), "Metode yang dimasukkan tidak valid");
                }
            }

            string resultString = "";

            // Jika tidak ada jalur
            if (path.Count == 0)
            {
                resultString += "Tidak ada jalur koneksi yang tersedia\nAnda harus memulai koneksi baru itu sendiri.";
            }
            // Ada jalur
            else
            {
                // Menambahkan jalur pada hasil
                foreach (string node in path)
                {
                    resultString += node;
                    if (node != path[path.Count - 1])
                    {
                        resultString += " -> ";
                    }
                }
                resultString += "\n";

                // Write Nth degree connection
                int N = path.Count - 2;
                resultString += N.ToString();
                if (N % 10 > 3 || (N % 100 >= 11 && N <= 13) || N % 10 == 0)
                {
                    resultString += "th - degree connection";
                }
                else
                {
                    int mod = N % 10;
                    switch (mod)
                    {
                        case 1:
                            resultString += "st-degree connection";
                            break;
                        case 2:
                            resultString += "nd-degree connection";
                            break;
                        case 3:
                            resultString += "rd-degree connection";
                            break;
                    }
                }
            }
            return new Tuple<List<string>, string>(path, resultString);
        }

        // Fitur Friend Recommendation
        public string FriendRecommendation(Vertex v)
        {
            Dictionary<string, List<string>> recommendation = new Dictionary<string, List<string>>();
            List<string> friends = new List<string>();

            foreach (Vertex friend in v.Edges)
            {
                friends.Add(friend.Name);
            }

            foreach (string friend in friends)
            {
                foreach (Vertex s in findVertex(friend).Edges)
                {
                    if (!recommendation.ContainsKey(s.Name) && !friends.Contains(s.Name) && !String.Equals(v.Name, s.Name))
                    {
                        recommendation.Add(s.Name, new List<string>());
                    }
                }
            }

            foreach (string recomFriend in recommendation.Keys)
            {
                foreach (Vertex mutual in findVertex(recomFriend).Edges)
                {
                    if (friends.Contains(mutual.Name)) recommendation[recomFriend].Add(mutual.Name);
                }
            }

            List<Tuple<string, int>> sortedKeys = new List<Tuple<string, int>>();

            foreach (string key in recommendation.Keys)
            {
                sortedKeys.Add(new Tuple<string, int>(key, recommendation[key].Count));
            }

            sortedKeys.Sort((a, b) => b.Item2.CompareTo(a.Item2));

            string result = "";

            if (recommendation.Count == 0)
            {
                result += "There is no friend recommendation for " + v.Name + "\n";
            }
            else
            {
                result += "List of friend recommendation for " + v.Name + "\n";
                foreach (Tuple<string, int> tuple in sortedKeys)
                {
                    result += "Account name: " + tuple.Item1 + "\n";
                    result += tuple.Item2 + " mutual friend(s):\n";

                    foreach (string mutual in recommendation[tuple.Item1])
                    {
                        result += mutual + "\n";
                    }
                    result += "\n";
                }
            }

            return result;
        }

    // Mengembalikan graf dalam bentuk graph MSAGL untuk divisualisasikan
    public Microsoft.Msagl.Drawing.Graph getMSAGLGraph(string name)
        {
            Microsoft.Msagl.Drawing.Graph g = new Microsoft.Msagl.Drawing.Graph(name);
            g.Directed = false;
            AdjacencyList.ForEach(v => g.AddNode(v.Name).Attr.Shape = Microsoft.Msagl.Drawing.Shape.Circle);

            foreach (Vertex v in AdjacencyList)
            {
                foreach (Vertex e in v.Edges)
                {
                    if (v.Name.CompareTo(e.Name) < 0)
                    {
                        Microsoft.Msagl.Drawing.Edge edge = g.AddEdge(v.Name, e.Name);
                        edge.Attr.ArrowheadAtTarget = Microsoft.Msagl.Drawing.ArrowStyle.None;
                        edge.Attr.Id = v.Name + e.Name;
                    }
                }
            }
            return g;
        }
    }
}
