class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original = image[sr][sc]

        if original == color:
            return image

        
        image[sr][sc] = color

        queue = deque()
        queue.append((sr, sc))

        while len(queue) > 0:
            r, c = queue.popleft()

            for nr, nc in [(r-1,c), (r+1, c), (r,c-1), (r,c+1)]:
                if 0<= nr < len(image) and 0<=nc<len(image[0]) and image[nr][nc] == original:
                    queue.append((nr,nc))
                    image[nr][nc] = color
        
        return image
