class Solution:
    def pick_sticks(self, heights, start, target):
        picked_indices = []
        total = 0
        n =len(heights)
        left = start - 1
        right = start
        pick_right = True
        while total < target:
            if pick_right and right < n:
                picked_indices.append(right)
                total += heights[right]
                right += 1
            elif not pick_right and left >= 0: 
                picked_indices.append(left)
                total += heights[left]
                left -= 1
               
            pick_right = not pick_right
            if right >= n and left < 0:
                break
        return picked_indices
    
def main():
    solution = Solution()
    heights = [10, 20, 25, 12, 35, 5, 8, 15, 16]
    start = 0
    target = 100
    result = solution.pick_sticks(heights, start, target)
    print("Indices of picked sticks:", result)

if __name__ == "__main__":
    main()
