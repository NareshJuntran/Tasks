import shutil
shutil.unpack_archive("/home/ubuntu/Downloads/tiny_shoppee_train.zip")


shutil.copytree('tiny_shoppee_train','copy')
shutil.make_archive('copy','zip','copy')
