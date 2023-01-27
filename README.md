# whisper-cc

Using OpenAI's Whisper for speech-to-text and ChatGPT generated code for converting Whisper output to SRT format captions.

The Whisper library already supports SRT formatting but this was more fun to ask ChatGPT to do it.

## Quickstart

Currently directly captioning video files is not supported yet and assumes the input file is a mp3 file.

```python
$ python pipeline.py audio.mp3 --size small
```

This will generate an SRT file for your audio in `outputs/subtitles.srt`.

The Whisper model can be optionally set with `--size` using the choices of `tiny`, `small`, `medium`, `large`.

## ChatGPT conversation for SRT helper functions

<img src=assets/chat-1.JPG width="768">

<img src=assets/chat-2.JPG width="768">

<img src=assets/chat-3.JPG width="768">

<img src=assets/chat-4.JPG width="768">

<img src=assets/chat-5.JPG width="768">

<img src=assets/chat-6.JPG width="768">

<img src=assets/chat-7.JPG width="768">

<img src=assets/chat-8.JPG width="768">