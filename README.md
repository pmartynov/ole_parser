### Instructions

1.Open terminal in project folder and enter the following code:

```
docker build -t ole_image .
```
If you run the command correctly, you'll see the following message:
```
Successfully tagged oleid_image:latest
```
2.Then enter the following:
   * Replace keys with your own keys

   * This command will create and run a Docker container and pass your AWS s3 access keys at the runtime as environment variables

```
docker run -e AWS_ACCESS_KEY_ID=your-key-id -e AWS_SECRET_ACCESS_KEY=your-secret-key -it --name ole_container ole_image
```