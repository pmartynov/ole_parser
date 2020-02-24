from time import time
from envs import envs
import oletools.oleid
import aioboto3
import asyncio
import boto3


async def main():
    async with aioboto3.resource('s3') as s3_resource:
        bucket = s3_resource.Bucket(name=envs.get("bucket_name"))
        tasks = []
        async for obj in bucket.objects.all():
            task = asyncio.create_task(download_file(s3_resource, bucket, obj))
            tasks.append(task)
        
        await asyncio.gather(*tasks)


async def download_file(s3, bucket, obj):
    await s3.Object(bucket.name, obj.key).download_file(obj.key)
    parse_file(obj.key)


def parse_file(filename):
    oid = oletools.oleid.OleID(filename)

    print('============== checking file %s ====================' % filename)
    indicators = oid.check()
    print('Have found %d possible threats in the %s file' % (len(indicators), filename))
    for i in indicators:
        print('\tIndicator id=%s name="%s" type=%s value=%s' % (i.id, i.name, i.type, repr(i.value)))
        print('\tdescription:', i.description)
        print('')

    print('====================================================')


if __name__ == '__main__':
    t0 = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time() - t0)
