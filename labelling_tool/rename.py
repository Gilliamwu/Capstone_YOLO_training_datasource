import glob, os
import re

def rename(dir, patterns, titlePattern, count=0):
	"""
	To rename every file in certain folder to make it five digit image.
	// if rename cause duplicate name, how? e.g. 2.jpg, 00002.jpg. rename of 2.jpg will cause replace of another one
	"""
	count_i = count
	for pattern in patterns:
		for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
			title, ext = os.path.splitext(os.path.basename(pathAndFilename))

			print("Find {}".format(title))
			os.rename(pathAndFilename, os.path.join(dir, titlePattern % (count_i)))
			count_i += 1
	    

#SAMPLE RUNNING CODE:
dir = "F:\\git_repositories\\BBox-Label-Tool\\Images\\003"
patterns = [r'*.jpg',r'*.png', r'*.JPEG']
titlePattern = r'%05d.JPEG'
count = 600
rename(dir, patterns, titlePattern, count=count)
