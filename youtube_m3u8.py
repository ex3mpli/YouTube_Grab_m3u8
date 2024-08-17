import os
import subprocess
import sys

def get_live_stream_info(youtube_url):
    try:
        # Use yt-dlp to fetch the stream URL
        result = subprocess.run(
            ['yt-dlp', '-g', youtube_url],
            capture_output=True, text=True, check=True
        )
        stream_url = result.stdout.strip()
        return stream_url
    except subprocess.CalledProcessError as e:
        print(f"Error fetching stream URL: {e.stderr}")
        return None

def generate_m3u8(stream_url, output_path):
    m3u8_content = f"#EXTM3U\n#EXTINF:-1,{'Live'}\n{stream_url}"

    try:
        with open(output_path, 'w') as m3u8_file:
            m3u8_file.write(m3u8_content)
        print(f"M3U8 file created at {output_path}")
    except IOError as e:
        print(f"Error writing M3U8 file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("YouTube Live M3U8 Grabbed!")
        sys.exit(1)

    youtube_url = sys.argv[1]
    output_m3u8 = sys.argv[2]

    stream_url = get_live_stream_info(youtube_url)
    if stream_url:
        generate_m3u8(stream_url, output_m3u8)
