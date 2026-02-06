from PIL import Image
import imageio.v3 as iio
import io
from pathlib import Path

def main():
    pass

# if __name__ == "__main__":
#     gif = Image.open('gifs/nyan-cat-rainbow.gif')
#     print(f"Loaded gif: {gif.format} {gif.size} ({gif.n_frames} frames)")

if __name__ == "__main__":
    reader = 'gifs/szk.webm'
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    for i, frame in enumerate(iio.imiter(reader)):
        output_path = output_dir / f"frame{i:05d}.jpg"
        iio.imwrite(output_path, frame)

    print("done")