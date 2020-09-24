chmod -R 755 .aws-sam/build/HelloWorldFunction/*
cd .aws-sam/build/HelloWorldFunction/
zip -r ../../../package.zip .