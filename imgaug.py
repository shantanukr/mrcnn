from keras.preprocessing import image 
import matplotlib.pyplot as plt

j=37
for j in range(37, 38):
    path="C:/Users/send8/Desktop/major/Fish_images/00"+str(j)+".jpeg"

    img=image.load_img(path,target_size=(512,512))
    img=image.img_to_array(img)

    x=img/255.0
    plt.imshow(x)
    plt.axis('off')
    #plt.show() 

    from keras.preprocessing.image import ImageDataGenerator
    gen=ImageDataGenerator(
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=0.2,
        vertical_flip=0.2,
        brightness_range=[0.2,1.0],
        fill_mode="nearest"
    )

    batch=x.reshape((1,*x.shape ))
    #print(batch.shape)
    print("hello"+str(j))

    i=0
    for out_batch in gen.flow(batch,batch_size=1,save_to_dir='fishv2', save_prefix='000', save_format='jpg'):
        plt.figure()
        imgplt=plt.imshow(image.img_to_array(out_batch[0]))
        i=i+1

        if i==10:
            break

        plt.axis("off")
    # plt.show()