import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    Kernels = {"Original": np.array([[0,0,0],
                                     [0,1,0],
                                     [0,0,0]], dtype=np.float32), 
               "Blur": (1/9)*np.array([[1,1,1],
                                     [1,1,1],
                                     [1,1,1]], dtype=np.float32), 
               "Gaussian blur": (1/16)*np.array([[1,2,1],
                                               [2,4,2],
                                               [1,2,1]], dtype=np.float32), 
               "Sharpen": np.array([[0,-1,0],
                                    [-1,5,-1],
                                    [0,-1,0]], dtype=np.float32), 
               "Sobel (x)": np.array([[-1,0,1],
                                      [-2,0,2],
                                      [-1,0,1]], dtype=np.float32), 
               "Sobel (y)": np.array([[-1,-2,-1],
                                      [0,0,0],
                                      [1,2,1]], dtype=np.float32), 
               "Edge detection": np.array([[-1,-1,-1],
                                           [-1,8,-1],
                                           [-1,-1,-1]], dtype=np.float32),
               "Emboss": np.array([[-2,-1,0],
                                   [-1,1,1],
                                   [0,1,2]], dtype=np.float32)}

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        # TODO: Implement internal variables
        self._names = list(self.kernels.keys())
        self._idx = 0  # 현재 선택된 커널 인덱스

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)

    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        return self._names[self._idx]

    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        self._idx = (self._idx + 1) % len(self._names)

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        self._idx = (self._idx - 1) % len(self._names)
