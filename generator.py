import time
from PIL import Image
from glob import glob
from numpy.random import choice
import os


class NFTGenerator:
    def __init__(self, input_dir, fps=1):
        self.input_dir = input_dir
        component = [p for p in os.listdir(self.input_dir) if not (p.startswith('.') or p.startswith('__'))]
        component = [glob(self.input_dir + f"/{c}/*") for c in component]
        self.component = [c for c in component if len(c) > 0]

    def generate(self, save_path=None, file_name=None, n_frame=1, unique=False):
        frames = []
        parts = []
        if not unique:
            for part in self.component:
                part_option = choice(part, 1)[0]
                parts.append(part_option)
        else:
            parts = list(next(self._options_product))

        for i in range(int(n_frame)):
            new_img = None
            for p in parts:
                if type(p) is list:
                    tmp = Image.open(p[i])
                else:
                    tmp = Image.open(p)
                if new_img is None:
                    new_img = tmp
                else:
                    new_img.paste(tmp, (0, 0), tmp)
            frames.append(new_img)
        if save_path is not None:
            if file_name is None:
                file_name = str(time.time())
            frames[0].save(f"{save_path}/{file_name}.png")
        return frames[0]
