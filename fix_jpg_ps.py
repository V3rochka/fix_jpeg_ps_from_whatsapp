from PIL import Image, ImageFilter
import os,sys

def main():
	#check args
	if len(sys.argv)!= 2:
		print("Wrong usage: {} $dir_path\n".format(sys.argv[0]))
		exit()

	dir_path=sys.argv[1]

	#check dir
	if os.path.exists(dir_path) == False:
		print("Path {} does not exist\n".format(dir_path))
		exit()

	#Go over the files in directory save as jpg every jpeg file
	for dirName, subdirList, fileList in os.walk(dir_path):
		print('Found directory: %s\n' % dirName)
		for fname in fileList:
			extension = os.path.splitext(fname)[1]
			if extension == '.jpeg':
				full_name_old = os.path.join(dirName, fname)
				new_name = os.path.splitext(fname)[0] + "_fixed.jpg"
				full_name_new =  os.path.join(dirName,new_name)
				im = Image.open(full_name_old)
				im.save(full_name_new, 'JPEG' )
				os.remove(full_name_old)
	print("DONE!")

if __name__ == "__main__":
	main()
