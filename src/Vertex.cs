using System;
using System.Collections.Generic;

namespace Tubes2
{    public class Vertex
    {
        // Name of the vertex
        public string Name
        {
            get;
            set;
        }


        // List of all the edges connected to the vertex
        public List<Vertex> Edges
        {
            get;
            set;
        }

        // Constructor
        public Vertex(string name)
        {
            this.Name = name;
            this.Edges = new List<Vertex>();
        }
    }
}