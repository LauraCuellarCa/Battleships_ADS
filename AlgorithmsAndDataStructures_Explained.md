# Battleships Algorithms and Data Structures
## Below you will find a more ind-depth look at the algorithms and data structures that we chose to implement our game. 


### Merge Sort - key aspect of our ranking system

We used this divide-and-conquer sorting algorithm by recursively dividing the player list into smaller halves until each subarray has only one sorted element. Then, it merges these sorted subarrays back together in a way that ensures the final merged array is sorted. The function is defined under the Rankings class. 

1. **Base Case:**
   - If the length of the `player_list` is greater than 1, the algorithm proceeds; otherwise, it considers the list already sorted.

2. **Divide:**
   - Find the middle index of the `player_list` (using integer division), creating two subarrays: `left_half` and `right_half`.

3. **Recursive Calls:**
   - Recursively apply the `merge_sort` function to both `left_half` and `right_half`. This step continues until the base case is reached for each subarray.

4. **Merge:**
   - Merge the sorted `left_half` and `right_half` back into the original `player_list`.
   - Initialize three indices: `i` for `left_half`, `j` for `right_half`, and `k` for the merged list.

5. **Comparisons and Merging:**
   - Compare the values at indices `i` and `j` in `left_half` and `right_half`, respectively.
   - If the element in `left_half` is greater, it is placed in the merged array at index `k`, and `i` is incremented.
   - If the element in `right_half` is greater or equal, it is placed in the merged array at index `k`, and `j` is incremented.
   - Increment `k` after placing an element in the merged array.

6. **Remaining Elements:**
   - After the above loop, one of the subarrays (`left_half` or `right_half`) may still have remaining elements.
   - Copy the remaining elements from both subarrays to the merged array.

The end result is that the `player_list` is now sorted based on the value of `['wins']` in the sub-dictionaries. The merging step ensures that the smaller sorted arrays are combined in a way that maintains overall order. This process is repeated until the entire list is sorted.
 
 **Code: (found in Rankings.py)**

    def merge_sort(self, player_list):    
        if len(player_list) > 1:
            mid = len(player_list) // 2
            left_half = player_list[:mid]
            right_half = player_list[mid:]
            self.merge_sort(left_half)
            self.merge_sort(right_half)
    
            i = j = k = 0
    
            while i < len(left_half) and j < len(right_half):
                if left_half[i][1]['wins'] > right_half[j][1]['wins']:
                    player_list[k] = left_half[i]
                    i += 1
                else:
                    player_list[k] = right_half[j]
                    j += 1
                k += 1
    
            while i < len(left_half):
                player_list[k] = left_half[i]
                i += 1
                k += 1
    
            while j < len(right_half):
                player_list[k] = right_half[j]
                j += 1
                k += 1


