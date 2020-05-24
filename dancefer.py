import argparse
import matplotlib

matplotlib.use('PS')

import visbeat
import os
import librosa


def main():
    dance = 'https://www.youtube.com/watch?v=4b64KyEFVhg'
    audio = 'https://www.youtube.com/watch?v=9DtI0TaEQoc'

    source_name = 'young-audrey'
    target_name = 'black-planet'
    output_path = './black-audrey.mp4'

    visbeat.SetAssetsDir('./VisBeatAssets/')

    source = visbeat.PullVideo(name=source_name,
                               source_location=dance,
                               max_height=None)
    target = visbeat.PullVideo(name=target_name,
                               source_location=audio,
                               max_height=None)

    synch_video_beat = 0
    synch_audio_beat = 0
    # nbeats = 400

    warped = visbeat.Dancefer(source_video=source,
                              target=target,
                              force_recompute=True,
                              warp_type='quad',
                              vbmark=False,
                              output_path=output_path,
                              nbeats=120)

    # warped.play()

    print("Your result was saved to: {}".format(warped.getPath()))

    # if os.path.exists(args.source):
    #     source_url = args.source
    # else:
    #     source_url = 'https://www.youtube.com/watch?v={}'.format(args.source)
    #
    # if os.path.exists(args.target):
    #     target_url = args.target
    # else:
    #     target_url = 'https://www.youtube.com/watch?v={}'.format(args.target)
    #
    # print("Source: {}\nTarget: {}".format(source_url, target_url))
    #
    # output_path = args.output_path
    # if output_path is None:
    #     output_path = './result.mp4'
    #
    # # files = librosa.util.find_files(
    # #     '/Users/johnbedalov/dev/src/visbeat/VisBeatAssets/VideoSources/vwnLp67rrzY/Versions/Original/maxheight_240/')
    # # y, sr = librosa.load(files[0])
    # # tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    #
    # result = visbeat.Dancefer(source_video=source_url,
    #                           target=target_url,
    #                           output_path=output_path,
    #                           force_recompute=True)
    # print("Result saved to {}".format(result.getPath()))


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("source",
    #                     help="Source video you want to warp. Can be a youtube vide id (get it from youtube urls 'https://www.youtube.com/watch?v=[VIDEO_ID]') or a path to a video file.")
    # parser.add_argument("target",
    #                     help="Target song. For now now use a video (will update later). Can be a youtube vide id or a path to a video file.)")
    # parser.add_argument("-o",
    #                     "--output_path",
    #                     help="path for the output file")
    # args = parser.parse_args()
    main()
