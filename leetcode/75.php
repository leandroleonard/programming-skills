<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function sortColors(&$nums) {
        $this->quicksort($nums, 0, count($nums) - 1);
    }

    function quicksort(&$arr, $left, $right)
    {
        if ($left < $right) {
            $pi = $this->partition($arr, $left, $right);
            $this->quicksort($arr, $left, $pi - 1);
            $this->quicksort($arr, $pi + 1, $right);
        }
    }

    function partition(&$arr, $left, $right): int
    {
        $pivot = $arr[$right];
        $i = $left - 1;
        for ($j = $left; $j < $right; $j++) {
            if($arr[$j] <= $pivot){
                $i++;
                $temp = $arr[$j];
                $arr[$j] = $arr[$i];
                $arr[$i] = $temp;
            }
        }
        $temp = $arr[$i + 1];
        $arr[$i+1] = $arr[$right];
        $arr[$right] = $temp;
        return $i + 1;
    }
}

$solution = new Solution();
$arr = [2,0,2,1,1,0];
$solution->sortColors($arr);
echo print_r($arr);