# blink_timelapse

Shoot timelapses with your [blink](https://blinkforhome.com) cameras.

## Getting started

You'll need to have [Docker](https://www.docker.com/products/docker-desktop) installed (unless you want to install blinkpy and mess with your global crontab).
You'll also need at least one blink camera.

## Credentials

First you can create a `secret.env` file at the same level as this `Readme.md`, with your `USERNAME` and `PASSWORD` for blink (or rename `secret.example`).

```bash
# /secret.env
USERNAME=my@email.com
PASSWORD=SomethingReallySecret
```

## Selecting cameras

To check that you can login, and what your cameras are named now you can run `make cameras`.
Docker will download the needed dependencies, and eventually you will see `app_1 |` followed by a camera name, and some information about it.

For every camera that you wish to capture in the timelapse, copy it's name and add it to `seceret.env`.
If you have multiple cameras, add a comma in between their names.

```bash
USERNAME=my@email.com
PASSWORD=SomethingReallySecret
CAMERAS=camera 1,camera 2
```

## Taking a test photo

Now that we have told it what cameras to use, we can run `make test-snap` and it will take a photo for each camera that we've added, and save it in the `images/` folder.

## Creating a crontab

If it was able to save a photo from each of your cameras, then you should decide on what kind of schedule you wish to use.

You probably don't want to shoot too often as that would drain the camera's battery relatively quickly.

To control the schedule we use a tool called [cron](https://en.wikipedia.org/wiki/Cron).

Here are some example cron patterns:

- `0 11,15,19,23 * * *` For hours 11, 15, 19, and 23, on the hour.
- `@hourly` Every hour, on the hour.
- `15 */4 * * *` 15 minutes past the hour, every 4th hour.

I would use the tool [crontab.guru](https://crontab.guru/#0_11,15,19,23_*_*_*) to figure out the schedule that you wish to use.

An additional wrench to throw in things, is that the process runs as the UTC time zone, so you'll have to adjust the hours to match.

Once you've figured out your crontab schedule (and crontab guru thinks its sane), you can edit `app/crontab`

```bash
# minute hour day(of month) month(day of week) command
# This is take a photo on the hour for hours 11, 15, 19, 23 UTC
0 11,15,19,23 * * * python /app/snap.py > /proc/1/fd/1 2>/proc/1/fd/2
```

Replace the `0 11,15,19,23` with your schedule, taking care to leave a space before `python /app/snap.py > /proc/1/fd/1 2>/proc/1/fd/2`.

## Run

Now we can start the schedule, and watch the `images/` folder fill up with pictures by running `make up`.

The logs will stay open so that you can see when a photo is taken or if there is an error.
If you hit `ctrl-c` or otherwise close the logs, it will keep running in the background.

When it's time to stop the timelapse, run `make down`.

## Video

While it's nice to have all those videos accessible in the directory to flip through, it would be even nicer to be able to make a video out of them.

To do that, you can run `make timelapse` which will convert all of the images to a video at `images/timelapse.mp4`.

If you have multiple cameras shooting timelapses in the same folder, the timelapse will try to make them all into the same video, so you should run it with only one camera's images in there at a time.
