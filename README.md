Mahjong
=======

A Mahjong solution try to find every possible way to win for a given patten of tile (13 in total) in hand.

Basic winning rules:

1. thirteen 1
2. seven pairs
3. one pair as eye with 4 combinations of any kind 


## A 'dragon-like' tile pattern

Tile in hand:   **1W  1W  1W  2W  3W  4W  5W  6W  7W  8W  9W  9W  9W**

out put:

```
combination:  1W  1W  1W 
combination:  1W  2W  3W 
combination:  4W  5W  6W 
combination:  7W  8W  9W 
eye:  9W 
Good point, you are on win state and the tile missing is:  1W 

combination:  1W  1W  1W 
combination:  9W  9W  9W 
combination:  3W  4W  5W 
combination:  6W  7W  8W 
eye:  2W 
Good point, you are on win state and the tile missing is:  2W 

combination:  9W  9W  9W 
combination:  1W  2W  3W 
combination:  3W  4W  5W 
combination:  6W  7W  8W 
eye:  1W 
Good point, you are on win state and the tile missing is:  3W 

combination:  1W  1W  1W 
combination:  2W  3W  4W 
combination:  4W  5W  6W 
combination:  7W  8W  9W 
eye:  9W 
Good point, you are on win state and the tile missing is:  4W 

combination:  1W  1W  1W 
combination:  9W  9W  9W 
combination:  2W  3W  4W 
combination:  6W  7W  8W 
eye:  5W 
Good point, you are on win state and the tile missing is:  5W 

combination:  9W  9W  9W 
combination:  1W  2W  3W 
combination:  4W  5W  6W 
combination:  6W  7W  8W 
eye:  1W 
Good point, you are on win state and the tile missing is:  6W 

combination:  1W  1W  1W 
combination:  2W  3W  4W 
combination:  5W  6W  7W 
combination:  7W  8W  9W 
eye:  9W 
Good point, you are on win state and the tile missing is:  7W 

combination:  1W  1W  1W 
combination:  9W  9W  9W 
combination:  2W  3W  4W 
combination:  5W  6W  7W 
eye:  8W 
Good point, you are on win state and the tile missing is:  8W 

combination:  9W  9W  9W 
combination:  1W  2W  3W 
combination:  4W  5W  6W 
combination:  7W  8W  9W 
eye:  1W 
Good point, you are on win state and the tile missing is:  9W 
```
