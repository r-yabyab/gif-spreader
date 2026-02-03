from PIL import Image

def main():
    pass

if __name__ == "__main__":
    gif = Image.open('gifs/nyan-cat-rainbow.gif')
    print(f"Loaded gif: {gif.format} {gif.size} ({gif.n_frames} frames)")