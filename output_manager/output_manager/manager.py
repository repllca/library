
import os
import json

class OutputManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        self.log_file = open(os.path.join(self.base_dir, 'log.txt'), 'a', encoding='utf-8')

    def print(self, *args, **kwargs):
        print(*args, **kwargs)
        print(*args, **kwargs, file=self.log_file, flush=True)

    def save_text(self, text, filename):
        with open(os.path.join(self.base_dir, filename), 'w', encoding='utf-8') as f:
            f.write(text)

    def save_json(self, data, filename):
        with open(os.path.join(self.base_dir, filename), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def save_figure(self, plt, filename):
        plt.savefig(os.path.join(self.base_dir, filename))
        plt.close()

    def close(self):
        self.log_file.close()
