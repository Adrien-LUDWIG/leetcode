class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        height, width = len(img), len(img[0])
        new_img = []

        for i in range(height):
            row = []

            for j in range(width):
                window_sum = 0
                window_count = 0
                
                for i_ in range(i-1, i+2):
                    for j_ in range(j-1, j+2):
                        if i_ < 0 or i_ >= height or j_ < 0 or j_ >= width:
                            continue

                        window_sum += img[i_][j_]
                        window_count += 1

                row.append(int(window_sum / window_count))
            
            new_img.append(row)
        
        return new_img
                




        