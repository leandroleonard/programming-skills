<?php

class ListNode
{
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null)
    {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution
{

    /**
     * @param ListNode $head
     * @return ListNode
     */
    function swapPairs($head) {
        if(!$head || !$head->next)
            return $head;

        $first = $head;
        $second = $head->next;

        $first->next = $this->swapPairs($second->next);
        $second->next = $first;

        return $second;
    }

    function addInFront($head, $value): ListNode
    {
        $newNode = new ListNode($value);

        if($head)
            $newNode->next = $head;

        return $newNode;
    }

    function addLast($head, $value): ListNode{
        $newNode = new ListNode($value);
        if(!$head) 
            return $newNode;

        $current = $head;
        while($current->next){
            $current = $current->next;
        }

        $current->next = $newNode;

        return $head;
    }

    function traverseList($head): void
    {
        while($head){
            echo "{$head->val} ";
            $head = $head->next;
        }
        echo PHP_EOL;
    }
}

$solution = new Solution();
$head = new ListNode(10);
$head = $solution->addLast($head, 20);
$head = $solution->addLast($head, 30);
$head = $solution->addLast($head, 40);

$solution->traverseList($head);
$head = $solution->swapPairs($head);
$solution->traverseList($head);
