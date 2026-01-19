<?php

class Graph
{
    public bool $directed;
    public array $adjList;

    function __construct(bool $directed = false)
    {
        $this->directed = $directed;
        $this->adjList = [];
    }

    function addNode($node){
        if(!isset( $this->adjList[$node]))
            $this->adjList[$node] = [];
    }

    function addEdge($source, $dest, $weight = null)
    {
        $this->addNode($source);
        $this->addNode($dest);

        $this->adjList[$source][] = [
            'node' => $dest,
            'weight' => $weight
        ];

        if(!$this->directed)
            $this->adjList[$dest][] = [
            'node' => $source,
            'weight' => $weight
        ];;

    }

    function getAdjList(): array
    {
        return $this->adjList;
    }

    function display(){
        foreach($this->adjList as $node => $edges){
            echo $node . " -> " ;
            foreach($edges as $edge){
                echo  "(" . $edge['node'] . ", " . ($edge['weight'] ?? 'null') . ") ";
            }
            echo PHP_EOL;
        }
    }
}

$graph = new Graph(false);

$graph->addEdge("A", "B", 10);
$graph->addEdge("A", "C", 5);
$graph->addEdge("C", "D", 7);

$graph->display();