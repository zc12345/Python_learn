import cv2
import numpy as np
import math

def get_heatmap(joints, target_size):
    maps = len(joints)
    height = 248
    width = 248
    sigma = 10.0
    heatmap = np.zeros((maps, height, width), dtype=np.float32)
    ##全部heatmap都初始化为0
    for idx, point in enumerate(joints):
        if point[0] < 0 or point[1] < 0: 
            continue
        put_heatmap(heatmap, idx, point, sigma)
    heatmap = heatmap.transpose((1, 2, 0)) ##self.height, self.width, CocoMetadata.__coco_parts
    # background
    heatmap[:, :, -1] = np.clip(1 - np.amax(heatmap, axis=2), 0.0, 1.0)  
    if target_size:
        heatmap = cv2.resize(heatmap, target_size, interpolation=cv2.INTER_AREA) #插值resize
    return heatmap.astype(np.float16)

def put_heatmap(heatmap, plane_idx, center, sigma):
    center_x, center_y = center
    _, height, width = heatmap.shape[:3]
    th = 4.6052
    delta = math.sqrt(th * 2)

    x0 = int(max(0, center_x - delta * sigma))
    y0 = int(max(0, center_y - delta * sigma))

    x1 = int(min(width, center_x + delta * sigma))
    y1 = int(min(height, center_y + delta * sigma))

    for y in range(y0, y1):
        for x in range(x0, x1):
            d = (x - center_x) ** 2 + (y - center_y) ** 2  
            exp = d / 2.0 / sigma / sigma  
            if exp > th:
                continue
            heatmap[plane_idx][y][x] = max(heatmap[plane_idx][y][x], math.exp(-exp))
            heatmap[plane_idx][y][x] = min(heatmap[plane_idx][y][x], 1.0)
            

if __name__ == "__main__":
    joints = np.array([
        [21,471],[145,429],[248,409],[372,367],[454,347],[537,326],
        [619, 306],[681,306],[867,306],[908,326],[970,347],[1012,367],
        [1074,388],[1156,388],[1197,409],[1259,429]
        ])#input image size: 1280*1024
    joints = joints/1280*248# resize joints coordinates
    target_size = (512, 512)# heatmap size
    hmap = get_heatmap(joints, target_size)
    heatmap = 255 * hmap
    heatmap = heatmap.astype(np.uint8)
    heatmaps = [heatmap[:,:,i] for i in range(heatmap.shape[2])]
    for i in range(heatmap.shape[2]):
        #cv2.imshow('image',heatmaps[i])
        cv2.imwrite('%s.jpg'%i, heatmaps[i])
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
