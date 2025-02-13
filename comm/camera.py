"""
  Script intended for obtaing data from a Real Sense Camera  
"""

import pyrealsense2 as rs
import numpy as np
import cv2

class RealSenseCamera:
  def __init__(self):
    self.pipeline = rs.pipeline()
    self.config = rs.config()
    self.pipeline_wrapper = rs.pipeline_wrapper(pipeline)
    self.pipeline_profile = config.resolve(pipeline_wrapper)
    
    width, height, freq = 640, 480, 30
    self.config.enable_stream(rs.stream.depth, width, height, rs.format.z16, freq)
    self.config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, freq)
    
  def get_single_frame():
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()
    if not depth_frame or not color_frame:
      get_single_frame()
    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    return depth_image, color_image

# Test Function for camera
def main():
  # Configure depth and color streams
  pipeline = rs.pipeline()
  config = rs.config()

  # Get device product line for setting a supporting resolution
  pipeline_wrapper = rs.pipeline_wrapper(pipeline)
  pipeline_profile = config.resolve(pipeline_wrapper)

  config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
  config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

  # Start streaming
  pipeline.start(config)

  try:
      while True:

          # Wait for a coherent pair of frames: depth and color
          frames = pipeline.wait_for_frames()
          depth_frame = frames.get_depth_frame()
          color_frame = frames.get_color_frame()
          if not depth_frame or not color_frame:
              continue

          # Convert images to numpy arrays
          depth_image = np.asanyarray(depth_frame.get_data())
          color_image = np.asanyarray(color_frame.get_data())

          # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
          depth_image = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

          cv2.imshow('RealSense_Depth', depth_image)
          cv2.imshow('RealSense_BGR', color_image)
          cv2.waitKey(1)

  finally:

      # Stop streaming
      pipeline.stop()


if __name__ == "__main__":
  main()
