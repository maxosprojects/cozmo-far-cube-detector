#!/usr/bin/env python3

import time, sys
import dlib
import numpy as np
import cozmo

# Load trained detector model
detector = dlib.simple_object_detector("detector.svm")
# Initialize window for results
win = dlib.image_window()

def displayImage(image):
	# Convert to numpy array
	img = np.array(image.raw_image)

	startTime = time.time()
	# Detect
	dets = detector(img)
	print('Took {:5.0f}'.format((time.time() - startTime) * 1000))

	win.clear_overlay()
	# Display raw Cozmo image
	win.set_image(img)
	# Display bounding rectangles
	win.add_overlay(dets)

def run(sdk_conn):
	'''The run method runs once Cozmo is connected.'''
	robot = sdk_conn.wait_for_robot()
	robot.camera.image_stream_enabled = True
	while(True):
		image = robot.world.latest_image
		# Cozmo may not immediately start video feed
		while image is None:
			image = robot.world.latest_image
			time.sleep(0.1)
		# Detect cubes and render image with bounding boxes
		displayImage(image)
		time.sleep(0.1)

if __name__ == '__main__':
	cozmo.setup_basic_logging()
	cozmo.robot.Robot.drive_off_charger_on_connect = False

	try:
		cozmo.connect(run)
	except cozmo.ConnectionError as e:
		sys.exit("A connection error occurred: %s" % e)
