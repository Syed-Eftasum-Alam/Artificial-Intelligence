def Genarator(image,noise):
    image= image+noise;
    return image;

def trainDiscriminator(discriminator[],data[],labels[],list[]):
   
    for i in range(len(discriminator)):
        discriminator[i].train(data, labels, list):
        list[i]= discriminator[i]   
    return list
                        
def useGAN(image,noise,discriminator[],data[],labels[],list[])
{
   trainDiscriminator(discriminator[],data[],labels[],list[])
   image1= Genarator(image,noise)
   for i in range(len(list)):  
        if(list[i].predict(image1)==1):
           return True
        else:
            list[i].train(image1,0)
    return False        
       
}


def main(){
    if(useGAN(image,noise,discriminator[],data[],labels[],list[])==True):
        print("Object matched")
    else:
        print("Object not matched")
}
