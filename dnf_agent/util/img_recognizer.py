import cv2
import numpy as np


class ImageRecognizer:
    def __init__(self, debug=False):
        self.debug = debug
        self.sift = cv2.SIFT_create()

    def find_image_location(self, original_image_path, image_to_find_path):
        original_image = cv2.imread(original_image_path, 0)
        image_to_find = cv2.imread(image_to_find_path, 0)

        kp1, des1 = self.sift.detectAndCompute(image_to_find, None)
        kp2, des2 = self.sift.detectAndCompute(original_image, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)

        if len(good_matches) < 4:
            print("Insufficient matches to calculate homography")
            return None

        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        h, w = image_to_find.shape

        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, H)

        center_x = (dst[0][0][0] + dst[2][0][0]) / 2
        center_y = (dst[0][0][1] + dst[2][0][1]) / 2

        if self.debug:
            result_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
            cv2.polylines(result_image, [np.int32(dst)], True, (0, 255, 0), 2)
            cv2.imwrite('../annotated_screenshot.jpg', result_image)
            cv2.imshow('Annotated Image', result_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return center_x, center_y

