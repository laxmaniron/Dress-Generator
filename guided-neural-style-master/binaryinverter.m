I = imread('./content__scale.jpg');
BW=im2bw(I,0.90);
BWinv=imcomplement(BW);
imwrite(BWinv,"./content__mask.jpg");

I = imread('./style__scale.jpg');
BW=im2bw(I,0.95);
BWinv=imcomplement(BW);
imwrite(BWinv,"./style__mask.jpg");